"""A progression game."""

from brain_games.launcher import launch
from brain_games.randomizer import random_int, random_progression

RULE = 'What number is missing in the progression?'


def start():
    """Launch the Progression game."""
    launch(generate_qa, RULE)


def generate_qa():
    """
    Generate a question and an answer of the game.

    Returns:
        (set): The pair of a question and an answer.
    """
    progression = random_progression()
    missing_index = random_int(0, len(progression))
    answer = progression[missing_index]
    progression[missing_index] = '..'
    question = ' '.join([str(elem) for elem in progression])

    return (question, answer)
