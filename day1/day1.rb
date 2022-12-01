# Advent of Code, Day 1 - https://adventofcode.com/2022/day/1

# Read input file input.txt
# Add up calories for each elf, separated by blank lines
# Store as highest number, if higher than previous
# Submit total for elf with most calories
#
# Part 2 - report total of top 3 elves

highest = 0
current = 0

lines = IO.readlines("input.txt")

lines.each do |line|
    if line.length > 1
        current += line.to_i
    else
        if current > highest
            highest = current
        end
        current = 0
    end
end

puts "Highest calorie load is %d." % [highest]