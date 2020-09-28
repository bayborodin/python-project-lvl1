"""A GCD game startup script."""
from brain_games.games import greatest_common_divisor as game
from brain_games.launcher import launch


def main() -> None:
    """Run the GCD game."""
    launch(game)


if __name__ == '__main__':
    main()
