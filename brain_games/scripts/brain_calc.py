"""A Calc game startup script."""
from brain_games.games import brain_calc_game as game
from brain_games.launcher import launch


def main() -> None:
    """Run the Calc game."""
    launch(game)


if __name__ == '__main__':
    main()
