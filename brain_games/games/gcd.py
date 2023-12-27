import random

TASK = "Find the greatest common divisor of given numbers."
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_gcd(a, b):
    while a >= 0 and b >= 0:
        if a == 0 or b == 0:
            return max(a, b)
        return get_gcd(b % a, a)


def get_question_and_answer():
    """Find the greatest common divisor of given numbers."""
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f"{num1} {num2}"
    correct_answer = str(get_gcd(num1, num2))
    return question, correct_answer
