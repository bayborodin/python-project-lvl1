"""An Even game."""
import random

import prompt


def run(user_name):
    """
    Launch an Even game.

    Parameters:
        user_name (str): The current user name.
    """
    is_winner = True
    samples = random.sample(range(1, 100), 3)
    for sample in samples:
        correct_answer = 'yes' if sample % 2 == 0 else 'no'
        print('Question: {0}'.format(sample))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                answer, correct_answer,
            ))
            is_winner = False
            break

    if is_winner:
        print('Congratulations, {0}!'.format(user_name))
