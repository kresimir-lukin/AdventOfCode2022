import sys

def score(char):
    return ord(char) - ord('a') + 1 if char.islower() else ord(char) - ord('A') + 27

def part1(rucksacks):
    priority_sum = 0
    for rucksack in rucksacks:
        first, second = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        intersection = set(first) & set(second)
        priority_sum += sum(map(score, intersection))
    return priority_sum

def part2(rucksacks):
    group_priority_sum = 0
    for i in range(0, len(rucksacks), 3):
        first, second, third = rucksacks[i], rucksacks[i+1], rucksacks[i+2]
        intersection = set(first) & set(second) & set(third)
        group_priority_sum += sum(map(score, intersection))
    return group_priority_sum

rucksacks = sys.stdin.read().splitlines()

print(f'Part 1: {part1(rucksacks)}, Part 2: {part2(rucksacks)}')