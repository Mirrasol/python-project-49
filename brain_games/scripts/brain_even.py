#!/usr/bin/env python3

from brain_games.games.even import TASK, game_even
from brain_games.logic import logic


def main():
    logic(TASK, game_even)


if __name__ == '__main__':
    main()
