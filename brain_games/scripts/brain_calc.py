#!/usr/bin/env python3

from brain_games.games import calc
from brain_games.logic import logic


def main():
    logic(calc.TASK, calc.game_calc)


if __name__ == '__main__':
    main()
