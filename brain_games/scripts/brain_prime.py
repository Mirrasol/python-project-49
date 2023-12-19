#!/usr/bin/env python3

from brain_games.games.prime import statement, game_prime
from brain_games.logic import logic


def main():
    logic(statement, game_prime)


if __name__ == '__main__':
    main()
