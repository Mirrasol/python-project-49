#!/usr/bin/env python3

from brain_games.games.gcd import TASK, game_gcd
from brain_games.logic import logic


def main():
    logic(TASK, game_gcd)


if __name__ == '__main__':
    main()
