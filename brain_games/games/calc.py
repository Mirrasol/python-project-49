import random


def game_calc():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    operator = random.choice(["+", "-", "*"])
    expression = f"{num1} {operator} {num2}"
    if operator == "+":
        correct_answer = str(num1 + num2)
    elif operator == "-":
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 * num2)
    return expression, correct_answer


statement = "What is the result of the expression?"
