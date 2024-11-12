"""
This module contains custom helpers for the Handlebars templating engine.
"""
import pybars
import datetime

def leet(this: pybars.Scope, value: str):
    """Converts a string to leet l33t 1337."""
    leet = {
        'a': '4',
        'b': '8',
        'e': '3',
        'g': '6',
        'l': '1',
        'o': '0',
        's': '5',
        't': '7',
        'z': '2'
    }
    return ''.join(leet.get(c, c) for c in value)

def capitalize(this: pybars.Scope, value: str):
    """Capitalizes the first letter of a string."""
    return value.capitalize()

def uppercase(this: pybars.Scope, value: str):
    """Converts a string to uppercase."""
    return value.upper()

def lowercase(this: pybars.Scope, value: str):
    """Converts a string to lowercase."""
    return value.lower()

def count(
    this: pybars.Scope, 
    options: dict, 
    starts: int = 2012, 
    ends = datetime.datetime.now().year
):
    """
    By default it generates a list of numbers 
    from 2012 to the current year.
    """
    items = [
        {'i': i, **this.context} 
        for i in range(starts, ends + 1)
    ]
    return [f'{options['fn'](item)}'.lstrip() for item in items]