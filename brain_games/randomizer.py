"""Common random functions."""

from random import SystemRandom

MAX_INT_SEQUENCE = 20


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


def random_int():
    """
    Generate a random integer number.

    Returns:
        (int) Random integer.
    """
    return SystemRandom().randint(0, MAX_INT_SEQUENCE)
