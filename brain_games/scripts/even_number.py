"""An Even game startup script."""
from brain_games.games import even_number as game
from brain_games.launcher import launch


def main() -> None:
    """Run the Even game."""
    launch(game)


if __name__ == '__main__':
    main()
