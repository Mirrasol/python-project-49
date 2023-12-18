from brain_games.is_even import is_even
import prompt


def game_even():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    result = is_even()
    if result:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
