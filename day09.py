import sys

def move(segments, direction):
    offsets = {'L': (-1, 0), 'U': (0, 1), 'R': (1, 0), 'D': (0, -1)}
    dx, dy = offsets[direction]
    segments[0][0] += dx
    segments[0][1] += dy
    for segment_index in range(1, len(segments)):
        previous = segments[segment_index-1]
        current = segments[segment_index]
        if max(abs(previous[0] - current[0]), abs(previous[1] - current[1])) > 1:
            if previous[0] != current[0]:
                current[0] += 1 if previous[0] > current[0] else -1
            if previous[1] != current[1]:
                current[1] += 1 if previous[1] > current[1] else -1

def simulate(moves, segment_count):
    segments = [[0, 0] for _ in range(segment_count)]
    tail_positions = set([tuple(segments[-1])])
    for direction, steps in moves:
        for _ in range(steps):
            move(segments, direction)
            tail_positions.add(tuple(segments[-1]))
    return len(tail_positions)

moves = sys.stdin.read().splitlines()
moves = [(move.split()[0], int(move.split()[1])) for move in moves]

print(f'Part 1: {simulate(moves, 2)}, Part 2: {simulate(moves, 10)}')