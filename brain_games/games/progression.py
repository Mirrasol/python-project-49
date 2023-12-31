import random

TASK = "What number is missing in the progression?"
MIN_NUMBER_PROGR = 2
MAX_NUMBER_PROGR = 100
PROGR_LENGTH = 10
MIN_NUMBER_DIFF = 2
MAX_NUMBER_DIFF = 5


def make_progression(start, difference):
    progression = [(start + (i - 1) * difference) for i in range(PROGR_LENGTH)]
    return progression


def hide_element(progression, hidden_index):
    new_progression = progression.copy()
    hidden_number = new_progression[hidden_index]
    new_progression[hidden_index] = ".."
    return new_progression, hidden_number


def get_question_and_answer():
    """What number is missing in the progression?"""
    start = random.randint(MIN_NUMBER_PROGR, MAX_NUMBER_PROGR)
    difference = random.randint(MIN_NUMBER_DIFF, MAX_NUMBER_DIFF)
    hidden_index = random.randint(0, PROGR_LENGTH - 1)
    progression = make_progression(start, difference)
    new_progression, hidden_number = hide_element(progression, hidden_index)
    question = " ".join(map(str, new_progression))
    correct_answer = str(hidden_number)
    return question, correct_answer
