"""A progression game."""

from random import SystemRandom

RULE = 'What number is missing in the progression?'
MAX_PROGRESSION_FIRST_TERM = 10
MIN_PROGRESSION_STEP = 1
MAX_PROGRESSION_STEP = 10
PROGRESSION_LENGTH = 10


def generate_qa():
    """
    Generate a question and an answer of the game.

    Returns:
        (set): The pair of a question and an answer.
    """
    progression = _get_random_progression()
    missing_index = SystemRandom().randint(0, len(progression) - 1)
    answer = progression[missing_index]
    progression[missing_index] = '..'
    question = ' '.join([str(elem) for elem in progression])

    return (question, answer)


def _get_random_progression():
    begin = SystemRandom().randint(0, MAX_PROGRESSION_FIRST_TERM)
    step = SystemRandom().randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
    last_number = begin + (step * PROGRESSION_LENGTH)

    return range(begin, last_number, step)
