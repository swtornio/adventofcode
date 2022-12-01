# Advent of Code, Day 1 - https://adventofcode.com/2022/day/1

# Read input file input.txt
# Add up calories for each elf, separated by blank lines
# Store as highest number, if higher than previous
# Submit total for elf with most calories

highest = 0
current = 0

with open("input.txt", "r") as f:
	for line in f:
		if line.strip() != '':
			# if line is not empty this should be true
			# cast to int and store in current
			current += int(line)
		else:
			# empty line means check if current is highest
			if current > highest:
				highest = current
			current = 0
			lines = 0

print(f"The most calories held by an elf is {highest}.")