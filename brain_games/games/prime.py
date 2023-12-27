import random

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 200


def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5 + 1)):
            if num % i == 0:
                return False
    return True


def get_question_and_answer():
    """Answer "yes" if given number is prime. Otherwise answer "no"."""
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = number
    correct_answer = 'no'
    if is_prime(number):
        correct_answer = 'yes'
    return question, correct_answer
