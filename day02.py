import sys

shape_points = {'A': 1, 'B': 2, 'C': 3}
game_points = {
    'AA': 3, 'AB': 6, 'AC': 0,
    'BA': 0, 'BB': 3, 'BC': 6,
    'CA': 6, 'CB': 0, 'CC': 3
}

def part1(rounds):
    xyz_to_abc = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    points = 0
    for opponent, me in rounds:
        me = xyz_to_abc[me]
        points += shape_points[me] + game_points[opponent + me]
    return points

def part2(rounds):
    win_lose_mapping = {
        'XA': 'C', 'XB': 'A', 'XC': 'B',
        'ZA': 'B', 'ZB': 'C', 'ZC': 'A'
    }
    points = 0
    for opponent, me in rounds:
        me = opponent if me == 'Y' else win_lose_mapping[me + opponent]
        points += shape_points[me] + game_points[opponent + me]
    return points

rounds = sys.stdin.read().splitlines()
rounds = list(map(lambda s: s.split(), rounds))

print(f'Part 1: {part1(rounds)}, Part 2: {part2(rounds)}')