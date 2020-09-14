"""An Even game startup script."""
from brain_games.games import brain_even_game as game
from brain_games.launcher import launch


def main():
    """Run the Even game."""
    launch(game)


if __name__ == '__main__':
    main()
