# Advent of Code, Day 2 - https://adventofcode.com/2022/day/2

#  First letter is their choice, point value is for the item
#  A Rock   1 point
#  B Paper  2 points
#  C Scissors  3 points
# 
#  Second letter is the outcome, have to set the right item
#  Z Win 6, Y Draw 3, X Loss 0

total = 0

with open("input.txt", "r") as f:
    for line in f:
        # they choose Rock
        if line[0] == 'A':
            if line[2] == 'X':
                total += 3 # 0 points for the loss, 3 for the scissors
            if line[2] == 'Y':
                total += 4 # 3 for the draw, 1 for the rock
            if line[2] == 'Z':
                total += 8 # 6 for the win, 2 for paper
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
                total += 2 # 0 points for the loss, 2 for the paper
            if line[2] == 'Y':
                total += 6 # 3 for the draw, 3 for the scissors
            if line[2] == 'Z':
                total += 7 # 6 for the win, 1 for the rock

print(f"Total points: {total}")
