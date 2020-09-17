"""The Prime Number game."""

from random import randint

MAX_INT_SEQUENCE = 20
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_qa():
    """
    Generate a question and an answer of the Prime game.

    Returns:
        (set): The pair of a question and an answer.
    """
    question = randint(0, MAX_INT_SEQUENCE - 1)  # noqa: S311 (not sec purpose)
    answer = 'yes' if _is_prime(question) else 'no'
    return (question, answer)


def _is_prime(num):
    """
    Check if the given number is prime.

    Parameters:
        num (int): A number to check.

    Returns:
        (str): Answer is a number prime or not.
    """
    if num < 2:
        return False
    for divider in range(2, num // 2):
        if num % divider == 0:
            return False
    return True
