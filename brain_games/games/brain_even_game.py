"""An Even game."""
from random import SystemRandom

MAX_INT_SEQUENCE = 20
RULES = 'Answer "yes" if number even otherwise answer "no".'


def generate_qa():
    """
    Generate a question and an answer of the Even game.

    Returns:
        (set): The pair of a question and an answer.
    """
    question = SystemRandom().randint(0, MAX_INT_SEQUENCE - 1)
    answer = 'yes' if question % 2 == 0 else 'no'
    return (question, answer)
