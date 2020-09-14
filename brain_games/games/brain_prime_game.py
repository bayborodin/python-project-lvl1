"""The Prime Number game."""

from random import SystemRandom

from brain_games.config import MAX_INT_SEQUENCE

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_qa():
    """
    Generate a question and an answer of the Prime game.

    Returns:
        (set): The pair of a question and an answer.
    """
    question = SystemRandom().randint(0, MAX_INT_SEQUENCE - 1)
    answer = _is_prime(question)
    return (question, answer)


def _is_prime(num):
    if num < 2:
        return 'no'
    for divider in range(2, num // 2):
        if num % divider == 0:
            return 'no'
    return 'yes'
