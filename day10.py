import sys

def part1(program):
    def _strength(cycle, x):
        return cycle * x if cycle in (20, 60, 100, 140, 180, 220) else 0
    strength, cycle, x = 0, 0, 1
    for command in program:
        cycle += 1
        strength += _strength(cycle, x)
        if command.startswith('addx'):
            cycle += 1
            strength += _strength(cycle, x)
            x += int(command.split()[1])
    return strength

def part2(program):
    display = [[' ']*40 for _ in range(6)]
    def _render(cycle, x):
        if x - 1 <= cycle % 40 <= x + 1:
            display[cycle // 40][cycle % 40] = '#'
    cycle, x = 0, 1
    for command in program:
        _render(cycle, x)
        cycle += 1
        if command.startswith('addx'):
            _render(cycle, x)
            cycle += 1
            x += int(command.split()[1])
    return '\n'.join(''.join(row) for row in display)

program = sys.stdin.read().splitlines()

print(f'Part 1: {part1(program)}, Part 2:\n{part2(program)}')