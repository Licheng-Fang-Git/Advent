import heapq
import numpy as np
file = open("input").readlines()

small_grid = []
for line in file:
    line = line.strip()
    one_row = []
    for item in line:
        one_row.append(int(item))
    small_grid.append(one_row)


def solve_one(grid):
    er,ec = len(grid)-1, len(grid[0])-1
    print(er,ec)
    pq = [(0,0,0)]
    visited = set()
    while pq:
        risk, r, c = heapq.heappop(pq)
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                continue
            if (nr, nc) in visited:
                continue
            if (nr, nc) == (er,ec):
                return risk + grid[nr][nc]
            visited.add((nr, nc))
            heapq.heappush(pq, (risk + grid[nr][nc], nr, nc))
    return 0


def expand():
    for index_row in range(len(expanded_grid)):
        for index_col in range(len(expanded_grid[0])):
            expanded_grid[index_row][index_col] =  small_grid[index_row%len(small_grid)][index_col%len(small_grid[0])] + index_col // len(small_grid[0]) + index_row//len(small_grid)
            if expanded_grid[index_row][index_col] >= 10:
                expanded_grid[index_row][index_col] -= 9


expanded_grid = [[0 for _ in range(len(small_grid[0]*5))] for _ in range(len(small_grid)*5)]
expand()

for row in expanded_grid:
    print(row)

print(solve_one(expanded_grid))