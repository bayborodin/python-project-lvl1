"""An Even game startup script."""

from brain_games import launcher
from games.brain_even_game import run


def main():
    """Run the Even game."""
    game_info = 'Answer "yes" if number even otherwise answer "no".'
    user_name = launcher.start_game(game_info)
    run(user_name)


if __name__ == 'main':
    main()
