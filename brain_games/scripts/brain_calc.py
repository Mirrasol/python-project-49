#!/usr/bin/env python3

from brain_games.games.calc import statement, game_calc
from brain_games.logic import logic


def main():
    logic(statement, game_calc)


if __name__ == '__main__':
    main()
