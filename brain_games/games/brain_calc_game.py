"""A calc game."""

from random import SystemRandom

MAX_INT_SEQUENCE = 20
RULES = 'What is the result of the expression?'


def generate_qa():
    """
    Generate a question and an answer of the Calc game.

    Returns:
        (set): The pair of a question and an answer.
    """
    operator = SystemRandom().choice(['+', '-', '*'])
    operands = SystemRandom().sample(range(0, MAX_INT_SEQUENCE), 2)
    question = '{0} {1} {2}'.format(
        operands[0], operator, operands[1],
    )
    answer = _calculate(operator, *operands)
    return (question, answer)


def _calculate(operator, operand_a, operand_b):
    """
    Apply operator to given operands.

    Parameters:
        operator (str): The symbol of ariphmetic operator.
        operand_a (int): The first operand.
        operand_b (int): The second operand.

    Returns:
        (int): The result of ariphmetic operation.

    Raises:
        ValueError: Unknown ariphmetic operator.
    """
    if operator == '+':
        return operand_a + operand_b
    elif operator == '-':
        return operand_a - operand_b
    elif operator == '*':
        return operand_a * operand_b

    raise ValueError('Unknown ariphmetic operator: {0}'.format(operator))
