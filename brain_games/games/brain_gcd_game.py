"""A GCD game."""

from random import SystemRandom

from brain_games.launcher import launch

RULE = 'Find the greatest common divisor of given numbers.'


def start():
    """Launch a GCD game."""
    launch(generate_qa, RULE)


def generate_qa():
    """
    Generate a question and an answer of the game.

    Returns:
        (set): The pair of a question and an answer.
    """
    operands = _get_random_operands()
    question = '{0} {1}'.format(*operands)
    answer = _get_gcd(*operands)
    return (question, answer)


def _get_random_operands():
    return SystemRandom().sample(range(1, 100), 2)


def _get_gcd(operand_a, operand_b):
    if operand_b == 0:
        return abs(operand_a)
    operand_c = operand_a % operand_b
    return _get_gcd(operand_b, operand_c)
