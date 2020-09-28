"""A GCD game."""
import random
from typing import Tuple

MAX_INT = 20
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_qa() -> Tuple[str, str]:
    """
    Generate a question and an answer of the GCF game.

    Returns:
        The pair of a question and an answer.
    """
    operands = random.sample(range(0, MAX_INT), 2)
    question = '{0} {1}'.format(*operands)
    answer = _gcd(operands[0], operands[1])
    return (question, str(answer))


def _gcd(num1: int, num2: int) -> int:
    """
    Find the greatest common factor of two numbers.

    Parameters:
        num1: The first integer number.
        num2: The second integer number.

    Returns:
        The greatest common factor.
    """
    if num2 == 0:
        return abs(num1)
    num3 = num1 % num2
    return _gcd(num2, num3)
