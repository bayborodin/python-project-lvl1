"""The Prime Number game."""

import random
from typing import Tuple

MAX_INT = 19
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_qa() -> Tuple[str, str]:
    """
    Generate a question and an answer of the Prime game.

    Returns:
        The pair of a question and an answer.
    """
    question = random.randint(0, MAX_INT)  # noqa: S311 (not sec purpose)
    answer = 'yes' if _is_prime(question) else 'no'
    return (question, str(answer))


def _is_prime(num: int) -> bool:
    """
    Check if the given number is prime.

    Parameters:
        num: A number to check.

    Returns:
        Answer is a number prime or not.
    """
    if num < 2:
        return False
    for divider in range(2, num // 2):
        if num % divider == 0:
            return False
    return True
