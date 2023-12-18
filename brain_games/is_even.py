from random import randint


def is_even():
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    for i in range(3):
        num = randint(1, 1000)
        print(f"Question: {num}")
        answer = input("Your answer: ")
        if num % 2 == 0:
            if answer == 'yes':
                print("Correct!")
            else:
                print(f"'{answer}' is wrong answer ;(.\
Correct answer was 'yes'.")
                return False
        else:
            if answer == 'no':
                print("Correct!")
            else:
                print(f"'{answer}' is wrong answer ;(.\
Correct answer was 'no'.")
                return False
    return True
