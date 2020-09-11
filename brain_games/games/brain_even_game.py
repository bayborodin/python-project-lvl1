"""An Even game."""

from brain_games.launcher import launch
from brain_games.randomizer import random_int

RULE = 'Answer "yes" if number even otherwise answer "no".'


def start():
    """Launch the Even game."""
    launch(generate_qa, RULE)


def generate_qa():
    """
    Generate a question and an answer of the game.

    Returns:
        (set): The pair of a question and an answer.
    """
    question = random_int()
    answer = _is_even(question)
    return (question, answer)


def _is_even(num):
    return 'yes' if num % 2 == 0 else 'no'
