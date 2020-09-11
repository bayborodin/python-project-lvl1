"""A calc game."""

from random import SystemRandom

from brain_games.launcher import launch

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
    operator = _get_random_operator()
    operands = _get_random_operands()
    question = '{0} {1} {2}'.format(
        operands[0], operator, operands[1],
    )
    answer = _get_answer(operator, *operands)
    return (question, answer)


def _get_answer(operator, operand_a, operand_b):
    if operator == '+':
        return operand_a + operand_b
    elif operator == '-':
        return operand_a - operand_b
    return operand_a * operand_b


def _get_random_operator():
    return SystemRandom().choice(['+', '-', '*'])


def _get_random_operands():
    return SystemRandom().sample(range(1, 100), 2)
