from collections import deque

file = open("../input").read().splitlines()

grid = []

for line in file:
    line = line.strip()
    one_row = []
    for item in line:
        one_row.append(item)
    grid.append(one_row)

def part_one(grid, sr, sc, sdr, sdc):
    q = deque([(sr,sc,sdr,sdc)])
    seen = set()
    while q:
        r, c, dr, dc = q.popleft()
        for nr, nc in [(r + dr, c + dc)]:
            if nr < 0 or nc  < 0 or nr >= len(grid) or nc >= len(grid[0]):
                continue
            if (nr,nc,dr,dc) in seen:
                continue
            seen.add((nr,nc,dr,dc))
            char = grid[nr][nc]
            if char == "." or char == "|" and dc == 0 or char == "-"  and dr == 0:
                q.append((nr, nc , dr, dc))

            elif char == "/":
                dr,dc = -dc, -dr
                q.append((nr, nc , dr, dc))

            elif char == "\\":
                dr, dc = dc, dr
                q.append((nr, nc , dr, dc))

            else:
                if char == "|":
                    for dr, dc in [(-1,0), (1,0)]:
                        q.append((nr, nc, dr, dc))

                elif char == "-":
                    for dr, dc in [(0,-1), (0,1)]:
                        q.append((nr, nc, dr, dc))


    electric = set()
    for r, c, _, _ in seen:
        electric.add((r, c))
    return electric

# electric = set()
# for r,c,_,_ in part_one(grid, 0, -1, 0, 1):
#     electric.add((r,c))

# print(len(electric))

def part_two():
    max_len = 0
    for column in range(len(grid[0])):
        max_len = max(max_len, len(part_one(grid, -1, column, 1, 0)))
        max_len = max(max_len, len(part_one(grid, len(grid), column, -1, 0)))

    for row in range(len(grid)):
        max_len = max(max_len, len(part_one(grid, row, -1, 0, 1)))
        max_len = max(max_len, len(part_one(grid, row, len(grid[0]), 0, -1)))

    return max_len

print(part_two())

