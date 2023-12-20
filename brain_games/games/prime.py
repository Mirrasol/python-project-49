import random


def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5 + 1)):
            if num % i == 0:
                return False
    return True


def game_prime():
    """Answer "yes" if given number is prime. Otherwise answer "no"."""
    num = random.randint(1, 200)
    expression = num
    correct_answer = 'no'
    if is_prime(num):
        correct_answer = 'yes'
    return expression, correct_answer


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
