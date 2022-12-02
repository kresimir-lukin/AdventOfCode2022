import sys

def get_sorted_elf_calories(calories):
    elf_calories = [0]
    for calorie in calories:
        if not calorie:
            elf_calories.append(0)
        elf_calories[-1] += int(calorie) if calorie else 0
    elf_calories.sort()
    return elf_calories

calories = sys.stdin.read().splitlines()

elf_calories = get_sorted_elf_calories(calories)
part1 = elf_calories[-1]
part2 = sum(elf_calories[-3:])

print(f'Part 1: {part1}, Part 2: {part2}')