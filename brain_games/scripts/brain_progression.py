#!/usr/bin/env python3

from brain_games.games import progression
from brain_games.logic import logic


def main():
    logic(progression.TASK, progression.game_progression)


if __name__ == '__main__':
    main()
