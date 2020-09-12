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


def ariphmetic_progression(begin, step, length):
    """
    Arithmetic progression generator.

    Parameters:
        begin (int): The start number fo progression.
        step (int): The step of progression.
        length (int): The length of progression.

    Returns:
        (list): List of the progression elements.
    """
    progression = []

    return _iterate(begin, step, length, progression)


def _iterate(_begin, _step, _length, acc):
    ib = _begin
    il = _length

    if il != 0:
        acc.append(ib)
        ib += _step
        il -= 1

        _iterate(ib, _step, il, acc)

    return acc
