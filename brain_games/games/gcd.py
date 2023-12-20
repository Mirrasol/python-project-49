import random


def gcd(a, b):
    while a >= 0 and b >= 0:
        if a == 0 or b == 0:
            return max(a, b)
        return gcd(b % a, a)


def game_gcd():
    """Find the greatest common divisor of given numbers."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    expression = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))
    return expression, correct_answer


TASK = "Find the greatest common divisor of given numbers."
