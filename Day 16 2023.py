from collections import deque

file = open("input").readlines()

grid = []

for line in file:
    one_row = []
    line = line.strip()
    for value in line:
        one_row.append(value)
    grid.append(one_row)

for row in grid:
    print(row)

def part_one(grid):
    q = deque([(0, -1, 0, 1)])
    seen = set()

    while q:
        r, c, dr, dc = q.popleft()
        print(r,c,dr,dc)
        for nr, nc in [(r + dr, c + dc)]:
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                continue
            char = grid[nr][nc]
            # dr = 1 if char = "|"  dc = 1 if char = "-"
            if char == "." or char == "|" and dr != 0 or char == "-" and dc != 0:
                if (nr, nc, dr, dc) not in seen:
                    q.append((nr, nc, dr, dc))
                    seen.add((nr, nc, dr, dc))
            if char == "/":
                # (0,1) --> (-1,0)   (0,-1) --> (1,0)
                dr, dc = -dc, -dr
                if (nr, nc, dr, dc) not in seen:
                    q.append((nr, nc, dr, dc))
                    seen.add((nr, nc, dr, dc))
            if char == "\\":
                # (0,1) --> (1,0)  (0,-1) --> (-1,0)
                dr, dc = dc, dr
                if (nr, nc, dr, dc) not in seen:
                    q.append((nr, nc, dr, dc))
                    seen.add((nr, nc, dr, dc))
            else:
                if char == "|":
                    for dr, dc in [(1, 0), (-1,0)]:
                        if (nr, nc, dr, dc) not in seen:
                            q.append((nr, nc, dr, dc))
                            seen.add((nr, nc, dr, dc))
                if char == "-":
                    for dr, dc in [(0,1),(0,-1)]:
                        if (nr, nc, dr, dc) not in seen:
                            q.append((nr, nc, dr, dc))
                            seen.add((nr, nc, dr, dc))

    return seen


print(len(part_one(grid)))

electric = set()

for r, c, _, _ in part_one(grid):
    electric.add((r,c))

print(len(electric))