#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    combinations = []

    def calc_rps(n: int, result: list):
        if n == 0:
            return combinations.append(result)
        for y in options:
            calc_rps(n-1, result + [y])
    calc_rps(n, [])
    print(combinations)
    return combinations


rock_paper_scissors(1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
