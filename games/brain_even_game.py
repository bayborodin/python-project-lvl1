import random
import prompt


def run(user_name):
    is_winner = True

    for _ in range(0, 3):
        num = random.randint(1, 100)
        correct_answer = 'yes' if num % 2 == 0 else 'no'
        print("Question: {0}".format(num))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print('\'{0}\' is wrong answer ;(. Correct answer was \'{1}\'.'.format(
                answer, correct_answer))
            is_winner = False
            break

    if is_winner:
        print('Congratulations, {0}!'.format(user_name))
