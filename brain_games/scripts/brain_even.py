#!/usr/bin/env python3

from brain_games.games import even
from brain_games.logic import logic


def main():
    logic(even.TASK, even.game_even)


if __name__ == '__main__':
    main()
