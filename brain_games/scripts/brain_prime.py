#!/usr/bin/env python3

from brain_games.games import prime
from brain_games.logic import logic


def main():
    logic(prime.TASK, prime.game_prime)


if __name__ == '__main__':
    main()
