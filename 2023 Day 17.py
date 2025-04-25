from collections import deque

file = open("input").readlines()
grid = []
for line in file:
    line = line.strip()
    one_row = []
    for num in line:
        one_row.append(num)
    grid.append(one_row)

for row in grid:
    print(row)


def part_one(grid):
    q = deque([(0, 1, grid[0][0])])
    seen = set()

    while q:
        r, c, h = q.popleft()
        seen.add((r, c))
        for nr, nc in [(r + 1, c + 0), (r, c + 1), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid):
                continue
            if (nr, nc) in seen:
                continue
            heat_loss = grid[nr][nc]
            optimal = float("inf")
            if heat_loss < optimal:
                optimal = heat_loss
                r = nr
                c = nc
                h += optimal
        q.append((r, c, h))


part_one(grid)
