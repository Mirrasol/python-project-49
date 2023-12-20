import random


def game_progression():
    """What number is missing in the progression?"""
    diff = random.randint(2, 5)
    start = random.randint(2, 100)
    choice_index = random.randint(0, 9)
    lst = [(start + (i - 1) * diff) for i in range(10)]
    correct_answer = str(lst[choice_index])
    lst[choice_index] = ".."
    expression = ""
    for i in range(10):
        expression += str(lst[i]) + ' '
    return expression, correct_answer
