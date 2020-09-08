"""Brain Games command-line user interface."""

import prompt


def welcome_user():
    """Ask a user name and print a greeting."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
