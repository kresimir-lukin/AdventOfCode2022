import sys, re

def part1(pairs):
    count_contained = 0
    for from1, to1, from2, to2 in pairs:
        count_contained += from1 <= from2 <= to2 <= to1 or from2 <= from1 <= to1 <= to2
    return count_contained

def part2(pairs):
    count_overlap = 0
    for from1, to1, from2, to2 in pairs:
        count_overlap += max(from1, from2) <= min(to1, to2)
    return count_overlap

pairs = []
for pair in sys.stdin.read().splitlines():
    re_match = re.match('(\d+)-(\d+),(\d+)-(\d+)', pair)
    pairs.append(tuple(map(int, re_match.groups())))

print(f'Part 1: {part1(pairs)}, Part 2: {part2(pairs)}')