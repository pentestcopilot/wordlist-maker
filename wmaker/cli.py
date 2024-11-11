import io
import re
import click
import helpers

from pybars import Compiler
from inspect import getmembers, isfunction

from __init__ import __version__

# Create a new instance of the Handlebars compiler
compiler = Compiler()

custom_helpers = {
    key: value 
    for key, value in getmembers(helpers, isfunction)
}

def extract_mustaches(template_content: str):
    # Matches {{variable}} or {{#if variable}}
    return set(re.findall(r"{{\s*(\w+)\s*}}", template_content))

epilog = """
All mustaches should be specified in the format --key value. For example,
if your template includes {{username}}, you should \
run the script like this:

wmaker template.hbs output.txt --username john
"""

CONTEXT_SETTINGS = dict(
    ignore_unknown_options=True,
    allow_extra_args=True,
    max_content_width=78
)

@click.command(
    epilog=epilog, 
    options_metavar='[options]',
    context_settings=CONTEXT_SETTINGS,
)
@click.argument('input', metavar='[input]', type=click.File('rb'))
@click.argument('output', metavar='[output]', type=click.File('wb'))
@click.version_option(
    __version__, 
    "-v", 
    "--version",
    message="%(version)s", 
    help="Output the current version of wordlist-maker."
)
@click.help_option(
    "-h", 
    "--help", 
    help="Show this message and exit."
)
@click.pass_context
def cli(
    ctx: click.Context,
    input: io.BufferedReader, 
    output: io.BufferedWriter, 
):
    kwargs = {
        ctx.args[i][2:]: ctx.args[i + 1] 
        for i in range(0, len(ctx.args), 2)
    }

    content = input.read().decode('utf-8')
    mustaches = extract_mustaches(content)

    if any(var not in kwargs for var in mustaches):
        raise click.ClickException(
            f"Missing required variables: {', '.join(mustaches - set(kwargs.keys()))}"
        )
    
    template = compiler.compile(content)
    result = template(kwargs, helpers=custom_helpers)

    output.write(result.encode('utf-8'))

if __name__ == "__main__":
    cli()
