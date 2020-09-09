"""Common Brain Games functions."""

import prompt


def start_game(game_info):
    """
    Show common info for all games and ask a player name.

    Parameters:
        game_info (str): The short game description.

    Returns:
        int:Player name
    """
    print('Welcome to the Brain Games!')
    print('{0}\n'.format(game_info))

    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))

    return name
