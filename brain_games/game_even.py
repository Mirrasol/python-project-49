from brain_games.is_even import is_even
from brain_games.welcome import welcome


def game_even():
    name = welcome()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    result = is_even()
    if result:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
