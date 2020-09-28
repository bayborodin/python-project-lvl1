"""A calc game."""

import random
from typing import Tuple

MAX_INT = 20
DESCRIPTION = 'What is the result of the expression?'


def generate_qa() -> Tuple[str, str]:
    """
    Generate a question and an answer of the Calc game.

    Returns:
        The pair of a question and an answer.
    """
    operator = random.choice(['+', '-', '*'])  # noqa: S311 (not sec purpose)
    operands = random.sample(range(0, MAX_INT), 2)
    question = '{0} {1} {2}'.format(
        operands[0], operator, operands[1],
    )
    answer = _calculate(operator, *operands)
    return (question, str(answer))


def _calculate(operator: str, operand_a: int, operand_b: int) -> int:
    """
    Apply operator to given operands.

    Parameters:
        operator: The symbol of ariphmetic operator.
        operand_a: The first operand.
        operand_b: The second operand.

    Returns:
        The result of ariphmetic operation.

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
