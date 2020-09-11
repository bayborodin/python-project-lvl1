"""A calc game."""

from brain_games.launcher import launch
from brain_games.randomizer import random_item, random_tuple

RULE = 'What is the result of the expression?'


def start():
    """Launch the Calc game."""
    launch(generate_qa, RULE)


def generate_qa():
    """
    Generate a question and an answer of the game.

    Returns:
        (set): The pair of a question and an answer.
    """
    operator = _random_operator()
    operands = random_tuple()
    question = '{0} {1} {2}'.format(
        operands[0], operator, operands[1],
    )
    answer = _calculate(operator, *operands)
    return (question, answer)


def _calculate(operator, operand_a, operand_b):
    if operator == '+':
        return operand_a + operand_b
    elif operator == '-':
        return operand_a - operand_b
    return operand_a * operand_b


def _random_operator():
    return random_item(['+', '-', '*'])
