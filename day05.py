import sys

def parse_crates(puzzle, start_index, end_index):
    crates = []
    for i in range(start_index, end_index):
        crate_index, puzzle_crate_index = 0, 1
        while puzzle_crate_index < len(puzzle[i]):
            if crate_index == len(crates):
                crates.append([])
            if puzzle[i][puzzle_crate_index] != ' ':
                crates[crate_index].append(puzzle[i][puzzle_crate_index])
            crate_index += 1
            puzzle_crate_index += 4
    return crates

def parse_moves(puzzle, start_index, end_index):
    moves = []
    for i in range(start_index, end_index):
        _, items, _, from_index, _, to_index = puzzle[i].split()
        moves.append(tuple(map(int, (items, from_index, to_index))))
    return moves

def move(crates, moves, reverse):
    crates = [crate[::-1] for crate in crates]
    for items, from_index, to_index in moves:
        to_append = []
        for _ in range(items):
            to_append.append(crates[from_index-1].pop())
        if reverse:
            to_append.reverse()
        crates[to_index-1].extend(to_append)
    return ''.join(crate[-1] for crate in crates)

puzzle = sys.stdin.read().splitlines()
divider_index = next(i for i, line in enumerate(puzzle) if not line)
crates = parse_crates(puzzle, 0, divider_index - 1)
moves = parse_moves(puzzle, divider_index + 1, len(puzzle))

part1 = move(crates, moves, False)
part2 = move(crates, moves, True)

print(f'Part 1: {part1}, Part 2: {part2}')