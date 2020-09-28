"""A Progression game startup script."""
from brain_games.games import arithmetic_progression as game
from brain_games.launcher import launch


def main() -> None:
    """Run the Progression game."""
    launch(game)


if __name__ == '__main__':
    main()
