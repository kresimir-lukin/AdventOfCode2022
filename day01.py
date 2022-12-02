import sys

calories = sys.stdin.read().splitlines()
elf_calories = [0]
for calorie in calories:
    if calorie:
        elf_calories[-1] += int(calorie)
    else:
        elf_calories.append(0)
elf_calories.sort()

part1 = elf_calories[-1]
part2 = sum(elf_calories[-3:])

print(f'Part 1: {part1}, Part 2: {part2}')