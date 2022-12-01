# Advent of Code, Day 1 - https://adventofcode.com/2022/day/1

# Read input file input.txt
# Add up calories for each elf, separated by blank lines
# Store as highest number, if higher than previous
# Submit total for elf with most calories
#
# Part 2 - report total of top 3 elves

highest = 0
current = 0
calorie_loads = list()

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
            calorie_loads.append(current)
            current = 0

# Sort the list of calorie loads in place
calorie_loads.sort(reverse=True)

print(f"The most calories held by an elf is {highest}.")
print(f"The top 3 calorie loads are {calorie_loads[0]}, {calorie_loads[1]}, and {calorie_loads[2]}.")
top_three_sum = calorie_loads[0] + calorie_loads[1] + calorie_loads[2]
print(f"The total calories of the top three is {top_three_sum}.")
