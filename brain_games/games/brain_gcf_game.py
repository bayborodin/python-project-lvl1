"""A GCD game."""

import math
from random import SystemRandom

from brain_games.config import MAX_INT_SEQUENCE

RULE = 'Find the greatest common divisor of given numbers.'


def generate_qa():
    """
    Generate a question and an answer of the GCF game.

    Returns:
        (set): The pair of a question and an answer.
    """
    operands = SystemRandom().sample(range(0, MAX_INT_SEQUENCE), 2)
    question = '{0} {1}'.format(*operands)
    answer = _gcd()
    return (question, answer)


def _gcd(num1, num2):
    """
    Find the greatest common factor of two numbers.

    Parameters:
        num1 (int): The first integer number.
        num2 (int): The second integer number.

    Returns:
        (int): The greatest common factor.
    """
    return math.gcd(num1, num2)
