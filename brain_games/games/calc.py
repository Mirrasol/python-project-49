import random

TASK = "What is the result of the expression?"
MIN_NUMBER = 1
MAX_NUMBER = 99


def get_question_and_answer():
    """What is the result of the expression?"""
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(["+", "-", "*"])
    question = f"{num1} {operator} {num2}"
    if operator == "+":
        correct_answer = str(num1 + num2)
    elif operator == "-":
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 * num2)
    return question, correct_answer
