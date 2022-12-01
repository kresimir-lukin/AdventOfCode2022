import sys

def max3_calories(calories):
    max1 = max2 = max3 = current = 0
    for calorie in calories + []:
        if not calorie:
            if current >= max1:
                max1, max2, max3 = current, max1, max2
            elif current >= max2:
                max2, max3 = current, max2
            elif current >= max3:
                max3 = current
        current = current + int(calorie) if calorie else 0
    return max1, max2, max3

assert len(sys.argv) == 2
calories = open(sys.argv[1]).read().splitlines()

print(f'Part 1: {max3_calories(calories)[0]}, Part 2: {sum(max3_calories(calories))}')