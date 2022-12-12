import sys, math, collections

def find(heightmap, letter):
    rows, cols = len(heightmap), len(heightmap[0])
    return [(r, c) for r in range(rows) for c in range(cols) if heightmap[r][c] == letter]

def height(r, c):
    if heightmap[r][c] == 'S':
        return ord('a')
    if heightmap[r][c] == 'E':
        return ord('z')
    return ord(heightmap[r][c])

def fewest_steps(heightmap, sr, sc, er, ec):
    rows, cols = len(heightmap), len(heightmap[0])
    steps = [[math.inf]*cols for _ in range(rows)]
    steps[sr][sc] = 0
    q = collections.deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and steps[nr][nc] == math.inf and height(nr, nc) <= height(r, c) + 1:
                steps[nr][nc] = steps[r][c] + 1
                q.append((nr, nc))
    return steps[er][ec]

heightmap = sys.stdin.read().splitlines()

startr, startc = find(heightmap, 'S')[0]
endr, endc = find(heightmap, 'E')[0]

part1 = fewest_steps(heightmap, startr, startc, endr, endc)
part2 = min(fewest_steps(heightmap, ra, ca, endr, endc) for ra, ca in find(heightmap, 'a'))

print(f'Part 1: {part1}, Part 2: {part2}')