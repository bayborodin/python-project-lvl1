"""Common mathematics functions."""


def gcf(val1, val2):
    """
    Find the greatest common factor of two numbers.

    Parameters:
        val1 (int): The first integer number.
        val2 (int): The second integer number.

    Returns:
        (int): Greatest common factor of given numbers.
    """
    if val2 == 0:
        return abs(val1)
    val3 = val1 % val2
    return gcf(val2, val3)
