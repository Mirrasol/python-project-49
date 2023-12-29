import prompt

AMOUNT_OF_ROUNDS = 3


def play(game):
    """Main functionality of the games."""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.TASK)
    for _ in range(AMOUNT_OF_ROUNDS):
        question, correct_answer = game.get_question_and_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        if correct_answer == user_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(.\
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
