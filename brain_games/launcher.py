"""Common Brain Games functions."""

import prompt

GAME_CYCLE_ATTEMPTS = 3  # number of attempts in the game


def _run_game_cycle(generate_qa, user_name):
    for _ in range(0, GAME_CYCLE_ATTEMPTS):  # noqa: WPS122 see bit.ly/3mrfIUh
        question, correct_answer = generate_qa()
        print('Question: {0}'.format(question))

        answer = prompt.string('Your answer: ')

        if answer != str(correct_answer):
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                answer, correct_answer,
            ))
            print("Let's try again, {0}!".format(user_name))
            return
        print('Correct!')

    print('Congratulations, {0}!'.format(user_name))


def launch(game):
    """
    Launch a game with a given rules.

    Parameters:
        game (function): The game logic function.
    """
    print('\nWelcome to the Brain Games!')
    print('{0}\n'.format(game.RULES))

    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(user_name))

    _run_game_cycle(game.generate_qa, user_name)
