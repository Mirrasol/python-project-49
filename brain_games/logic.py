from brain_games.welcome import welcome


def logic(line, game):
    name = welcome()
    print(line)
    for _ in range(3):
        expression, correct_answer = game()
        print(f"Question: {expression}")
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
