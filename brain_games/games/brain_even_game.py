"""An Even game."""

from random import SystemRandom

from brain_games.launcher import launch

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
    question = _get_random_number()
    answer = _is_even(question)
    return (question, answer)


def _get_random_number():
    return SystemRandom().randint(1, 100)


def _is_even(num):
    return 'yes' if num % 2 == 0 else 'no'
