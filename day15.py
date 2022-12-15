import sys, re

def part1(sensor_beacon):
    nonbeacon, row = set(), search_space // 2
    for (sx, sy), (bx, by) in sensor_beacon:
        diff = abs(sx - bx) + abs(sy - by)
        diff_row = abs(sy - row)
        for p in range(diff - diff_row + 1):
            nonbeacon.add((sx - p, row))
            nonbeacon.add((sx + p, row))
    beacons = set(beacon for _, beacon in sensor_beacon)
    return len(nonbeacon.difference(beacons))

def part2(sensor_beacon):
    def _find_non_excluded(excluded_intervals):
        candidate = 0
        for f, t in sorted(excluded_intervals):
            if f > candidate:
                return candidate
            candidate = max(candidate, t + 1)
        return candidate if candidate <= search_space else -1
    x = y = -1
    for step in range(search_space + 1):
        excludex, excludey = [], []
        for (sx, sy), (bx, by) in sensor_beacon:
            diff = abs(sx - bx) + abs(sy - by)
            if diff >= abs(step - sy):
                diffy = diff - abs(step - sy)
                excludey.append((max(sx - diffy, 0), min(sx + diffy, search_space)))
            if diff >= abs(step - sx):
                diffx = diff - abs(step - sx)
                excludex.append((max(sy - diffx, 0), min(sy + diffx, search_space)))
        y = max(y, _find_non_excluded(excludex))
        x = max(x, _find_non_excluded(excludey))
    return x * 4000000 + y

search_space = 4000000
sensor_beacon = []
for line in sys.stdin.read().splitlines():
    re_match = re.match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
    sx, sy, bx, by = map(int, re_match.groups())
    sensor_beacon.append(((sx, sy), (bx, by)))

print(f'Part 1: {part1(sensor_beacon)}, Part 2: {part2(sensor_beacon)}')