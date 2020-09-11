"""A GCD game."""

from brain_games.game_math import gcf
from brain_games.launcher import launch
from brain_games.randomizer import random_tuple

RULE = 'Find the greatest common divisor of given numbers.'


def start():
    """Launch a GCD game."""
    launch(generate_qa, RULE)


def generate_qa():
    """
    Generate a question and an answer of the game.

    Returns:
        (set): The pair of a question and an answer.
    """
    operands = random_tuple()
    question = '{0} {1}'.format(*operands)
    answer = gcf(*operands)
    return (question, answer)
