"""A Brain Games startup script."""

from brain_games.cli import welcome_user


def main():
    """Run the brain games."""
    print('Welcome to the Brain Games!\n')
    welcome_user()


if __name__ == '__main__':
    main()
