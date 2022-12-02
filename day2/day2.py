# Advent of Code, Day 2 - https://adventofcode.com/2022/day/2

#  A Rock X   1 point
#  B Paper Y  2 points
#  C Scissors Z  3 points
# 
#  Win 6, Draw 3, Loss 0

total = 0

with open("input.txt", "r") as f:
    for line in f:
        # they choose Rock
        if line[0] == 'A':
            if line[2] == 'X':
                total += 4 # 3 points for the draw, 1 for the rock
            if line[2] == 'Y':
                total += 8 # 6 for the win, 2 for the paper
            if line[2] == 'Z':
                total += 3 # 0 for the loss, 3 for the scissors
        # they choose paper
        if line[0] == 'B':
            if line[2] == 'X':
                total += 1 # 0 points for the loss, 1 for the rock
            if line[2] == 'Y':
                total += 5 # 3 for the draw, 2 for the paper
            if line[2] == 'Z':
                total += 9 # 6 for the win, 3 for the scissors
        # they choose scissors
        if line[0] == 'C':
            if line[2] == 'X':
                total += 7 # 6 points for the win, 1 for the rock
            if line[2] == 'Y':
                total += 2 # 0 for the loss, 2 for the paper
            if line[2] == 'Z':
                total += 6 # 3 for the draw, 3 for the scissors

print(f"Total points: {total}")
