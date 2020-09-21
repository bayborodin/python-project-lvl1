"""A progression game."""

import random
from typing import List, Tuple

RULES = 'What number is missing in the progression?'
MAX_PROGRESSION_FIRST_TERM = 10
MIN_PROGRESSION_STEP = 1
MAX_PROGRESSION_STEP = 10
PROGRESSION_LENGTH = 10


def generate_qa() -> Tuple[str, str]:
    """
    Generate a question and an answer of the Progression game.

    Returns:
        The pair of a question and an answer.
    """
    progression = _get_random_progression()
    missing_index = random.randint(0, len(progression) - 1)  # noqa: S311
    answer = progression[missing_index]
    progression[missing_index] = '..'
    question = ' '.join(str(elem) for elem in progression)

    return (question, str(answer))


def _get_random_progression() -> List[int]:
    """
    Generate random ariphmetic progression.

    Returns:
        Random ariphmetic progression.
    """
    begin = random.randint(0, MAX_PROGRESSION_FIRST_TERM)  # noqa: S311
    step = random.randint(  # noqa: S311
        MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP,
    )
    last_number = begin + (step * PROGRESSION_LENGTH)

    return list(range(begin, last_number, step))
