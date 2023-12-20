import random


def game_prime():
    """Answer 'yes' if given number is prime. Otherwise answer 'no'."""
    num = random.randint(1, 200)
    expression = num
    correct_answer = "yes"
    if num == 1:
        correct_answer = "no"
    else:
        for i in range(2, int(num ** 0.5 + 1)):
            if num % i == 0:
                correct_answer = "no"
                break
    return expression, correct_answer


TASK = "Answer 'yes' if given number is prime. Otherwise answer 'no'."
