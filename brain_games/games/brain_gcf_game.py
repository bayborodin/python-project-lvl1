"""A GCD game."""

import math
from random import SystemRandom

from brain_games.config import MAX_INT_SEQUENCE

RULE = 'Find the greatest common divisor of given numbers.'


def generate_qa():
    """
    Generate a question and an answer of the game.

    Returns:
        (set): The pair of a question and an answer.
    """
    operands = _random_tuple()
    question = '{0} {1}'.format(*operands)
    answer = _gcd()
    return (question, answer)


def _random_tuple():
    return SystemRandom().sample(range(0, MAX_INT_SEQUENCE), 2)


def _gcd(num1, num2):
    return math.gcd(num1, num2)
