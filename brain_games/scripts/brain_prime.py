#!/usr/bin/env python3

from brain_games.games.prime import TASK, game_prime
from brain_games.logic import logic


def main():
    logic(TASK, game_prime)


if __name__ == '__main__':
    main()
