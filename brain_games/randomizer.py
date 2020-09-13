"""Common random functions."""

from random import SystemRandom

from brain_games.game_math import ariphmetic_progression as ap

MAX_INT_SEQUENCE = 20
MAX_PROGRESSION_FIRST_TERM = 10
MAX_PROGRESSION_STEP = 10
MIN_PROGRESSION_STEP = 1
PROGRESSION_LENGTH = 10


def random_item(collection):
    """
    Select a random item of the given collection.

    Parameters:
        collection (list): collection from which to select a random item.

    Returns:
        (obj): Randomly selected item.
    """
    return SystemRandom().choice(collection)


def random_tuple():
    """
    Generate a random tuple of two ints.

    Returns:
        (tuple): Tuple of two integers.
    """
    return SystemRandom().sample(range(0, MAX_INT_SEQUENCE), 2)


def random_int(begin=0, end=None):
    """
    Generate a random integer number.

    Parameters:
        begin (int): The main value of random.
        end (int): The max value of random.

    Returns:
        (int) Random integer.
    """
    if not end:
        end = MAX_INT_SEQUENCE

    return SystemRandom().randint(begin, end - 1)


def random_progression():
    """
    Generate a random ariphmetic progression.

    Returns:
        (list): Progression numbers sequence
    """
    first_term = SystemRandom().randint(0, MAX_PROGRESSION_FIRST_TERM)
    step = SystemRandom().randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)

    return ap(first_term, step, PROGRESSION_LENGTH)
