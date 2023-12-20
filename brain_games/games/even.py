import random


def game_even():
    """Answer "yes" if the number is even, otherwise answer "no"."""
    expression = random.randint(1, 1000)
    if expression % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return expression, correct_answer


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
