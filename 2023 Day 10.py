from collections import deque

file = open("input").readlines()
grid = []
tr = -1
tc = -1

for line in file:
    one_row = []
    tr += 1
    tc = -1
    for item in line.strip():
        one_row.append(item)
        tc += 1
        if item == "S":
            sr,sc = tr,tc
    grid.append(one_row)

for row in grid:
    print(row)

print()
loop_grid = [["." for _ in range(len(grid[0]))] for r in range(len(grid))]

def part_one():
    q = deque([(sr, sc, 0, 1, 0)])
    seen = {sr, sc, 1, 0}

    while q:
        r, c, dr, dc, n = q.pop()
        loop_grid[r][c] = grid[r][c]
        nr =  r + dr
        nc =  c + dc
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]): continue
        if (nr, nc, dr, dc) in seen: continue
        seen.add((nr,nc,dr,dc))
        ch = grid[nr][nc]
        if ch == ".":
            continue
        if ch == "|":
            if dc == 0 :
                q.append((nr, nc, dr, dc, n + 1))
            else:
                continue
        elif ch == "-":
            if dr == 0:
                q.append((nr, nc, dr, dc, n + 1))
            else:
                continue
        elif ch == "L":
            q.append((nr, nc, dc, dr, n + 1))

        elif ch == "J":
            if (dr,dc) == (1,0):
                q.append((nr, nc, dc, -dr, n + 1))
            if (dr,dc) == (0,1):
                q.append((nr, nc, -dc, dr, n + 1))
        elif ch == "7":
            q.append((nr, nc, dc, dr, n + 1))
        elif ch == "F":
            if (dr,dc) == (0,-1):
                q.append((nr, nc, -dc, dr, n + 1))
            if (dr,dc) == (-1,0):
                q.append((nr, nc, dc, -dr, n + 1))
        if ch == "S":

            return (n + 1)/ 2




print(part_one())

for row in loop_grid:
    print(row)

up = None
num = [0,1,2]

for ch in num:
    print(ch)
    if ch == 0:
        assert up is None
    if ch == 1:
        assert up is not None
    print("check?")
    if ch == 2 :
        assert up is None
    else:
        raise RuntimeError("Nope")