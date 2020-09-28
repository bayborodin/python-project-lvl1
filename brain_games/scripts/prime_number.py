"""A Prime Number game startup script."""
from brain_games.games import prime_number as game
from brain_games.launcher import launch


def main() -> None:
    """Run the Prime Number game."""
    launch(game)


if __name__ == '__main__':
    main()
