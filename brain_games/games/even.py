import random

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 1000


def is_even(num):
    return num % 2 == 0


def get_question_and_answer():
    """Answer "yes" if the number is even, otherwise answer "no"."""
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = number
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
