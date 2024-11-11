"""
This module contains custom helpers for the Handlebars templating engine.
"""
import pybars

def leet(this: pybars.Scope, value: str):
    """Converts a string to leet speak."""
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