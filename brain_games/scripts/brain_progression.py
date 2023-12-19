#!/usr/bin/env python3

from brain_games.games.progression import statement, game_progression
from brain_games.logic import logic


def main():
    logic(statement, game_progression)


if __name__ == '__main__':
    main()
