import sys

def marker_position(signal, size):
    marker_candidate = ''
    for i, char in enumerate(signal):
        marker_candidate = (marker_candidate + char)[-size:]
        if len(set(marker_candidate)) == size:
            return i + 1

signal = sys.stdin.read()

part1 = marker_position(signal, 4)
part2 = marker_position(signal, 14)

print(f'Part 1: {part1}, Part 2: {part2}')