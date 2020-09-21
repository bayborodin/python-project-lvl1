"""An Even game."""
import random
from typing import Tuple

MAX_INT = 20
RULES = 'Answer "yes" if number even otherwise answer "no".'


def generate_qa() -> Tuple[str, str]:
    """
    Generate a question and an answer of the Even game.

    Returns:
        The pair of a question and an answer.
    """
    question = random.randint(0, MAX_INT - 1)  # noqa: S311 (not sec purpose)
    answer = 'yes' if question % 2 == 0 else 'no'
    return (question, str(answer))
