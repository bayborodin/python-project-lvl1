"""A calc game."""

from random import SystemRandom

import prompt


def run(user_name):
    """
    Launch a Calc game.

    Parameters:
        user_name (str): The current user name.
    """
    cnt = 3
    while cnt > 0:
        cnt -= 1

        operator = _get_random_operator()
        operands = _get_random_operands()
        correct_answer = _calculate(operator, *operands)

        print('Question: {0} {1} {2}'.format(
            operands[0], operator, operands[1],
        ))
        answer = prompt.integer('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                answer, correct_answer,
            ))
            print("Let's try again, {0}!".format(user_name))
            break
    else:
        print('Congratulations, {0}!'.format(user_name))


def _calculate(operator, operand_a, operand_b):
    if operator == '+':
        return operand_a + operand_b
    elif operator == '-':
        return operand_a - operand_b
    return operand_a * operand_b


def _get_random_operator():
    rnd = SystemRandom()
    return rnd.choice(['+', '-', '*'])


def _get_random_operands():
    rnd = SystemRandom()
    return rnd.sample(range(1, 100), 2)
