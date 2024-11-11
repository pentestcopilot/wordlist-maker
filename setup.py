from setuptools import setup, find_packages
from wmaker import __version__

from setuptools import find_packages, setup

setup(
    name='wordlist-maker',
    description='Generate smart wordlists using hbs for password cracking.',
    version=__version__,
    packages=find_packages(),
    license="MIT",
    url="https://github.com/pentestcopilot/wordlist-maker",
    entry_points={
        'console_scripts': ['wmaker = wmaker.cli.cli:entry_point']
    },
    setup_requires=['setuptools'],
    python_requires='>=3.9',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Security',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)