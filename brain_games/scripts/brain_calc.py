"""A Calc game startup script."""

from brain_games import launcher
from brain_games.games.brain_calc_game import run


def main():
    """Run the Calc game."""
    game_info = 'What is the result of the expression?'
    user_name = launcher.start_game(game_info)
    run(user_name)


if __name__ == '__main__':
    main()
