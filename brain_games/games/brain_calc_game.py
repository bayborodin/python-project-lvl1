"""A calc game."""

from random import SystemRandom

from brain_games.config import MAX_INT_SEQUENCE

RULE = 'What is the result of the expression?'


def generate_qa():
    """
    Generate a question and an answer of the game.

    Returns:
        (set): The pair of a question and an answer.
    """
    operator = _random_operator()
    operands = _random_tuple()
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
    return SystemRandom().choice(['+', '-', '*'])


def _random_tuple():
    return SystemRandom().sample(range(0, MAX_INT_SEQUENCE), 2)
