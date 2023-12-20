import prompt


def welcome():
    """Post a welcoming message and ask user for their name."""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name
