import sys

def left(forest, row, col):
    col_left = col - 1
    while col_left >= 0 and forest[row][col_left] < forest[row][col]:
        col_left -= 1
    return col - col_left - 1

def up(forest, row, col):
    row_up = row - 1
    while row_up >= 0 and forest[row_up][col] < forest[row][col]:
        row_up -= 1
    return row - row_up - 1

def right(forest, row, col):
    col_right = col + 1
    while col_right < len(forest[0]) and forest[row][col_right] < forest[row][col]:
        col_right += 1
    return col_right - col - 1

def down(forest, row, col):
    row_down = row + 1
    while row_down < len(forest) and forest[row_down][col] < forest[row][col]:
        row_down += 1
    return row_down - row - 1

def solve(forest):
    rows, cols = len(forest), len(forest[0])
    visible = max_scenic_score = 0
    for row in range(rows):
        for col in range(cols):
            l, u, r, d = left(forest, row, col), up(forest, row, col), right(forest, row, col), down(forest, row, col)
            left_edge = l == col
            up_edge = u == row
            right_edge = r == cols-col-1
            down_edge = d == rows-row-1
            visible += left_edge or up_edge or right_edge or down_edge
            scenic_score = (l + (not left_edge)) * (u + (not up_edge)) * (r + (not right_edge)) * (d + (not down_edge))
            max_scenic_score = max(max_scenic_score, scenic_score)
    return visible, max_scenic_score

forest = sys.stdin.read().splitlines()

part1, part2 = solve(forest)

print(f'Part 1: {part1}, Part 2: {part2}')