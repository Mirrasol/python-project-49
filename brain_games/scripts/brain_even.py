#!/usr/bin/env python3

from brain_games.games.even import statement, game_even
from brain_games.logic import logic


def main():
    logic(statement, game_even)


if __name__ == '__main__':
    main()
