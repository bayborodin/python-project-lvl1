"""Common Brain Games functions."""

import prompt

GAME_CYCLE_ATTEMPTS = 3  # number of attempts in the game


def _show_game_rule(rule):
    print('\nWelcome to the Brain Games!')
    print('{0}\n'.format(rule))


def _ask_user_name():
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    return name


def _get_answer(correct_answer):
    if isinstance(correct_answer, str):
        answer = prompt.string('Your answer: ')
    else:
        answer = prompt.integer('Your answer: ')
    return answer


def _end_game_loss(user_name):
    print("Let's try again, {0}!".format(user_name))


def _end_game_win(user_name):
    print('Congratulations, {0}!'.format(user_name))


def _run_game_cycle(generate_qa, user_name):
    for _ in range(0, GAME_CYCLE_ATTEMPTS):  # noqa: WPS122
        question, correct_answer = generate_qa()
        print('Question: {0}'.format(question))

        answer = _get_answer(correct_answer)

        if answer != correct_answer:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                answer, correct_answer,
            ))
            _end_game_loss(user_name)
            return
        print('Correct!')

    _end_game_win(user_name)


def launch(game):
    """
    Launch a game with a given rule.

    Parameters:
        game (function): The game logic function.
    """
    _show_game_rule(game.RULE)
    user_name = _ask_user_name()
    _run_game_cycle(game.generate_qa, user_name)
