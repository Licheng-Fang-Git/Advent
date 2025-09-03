from collections import deque

file = open("../input")
lines = file.readlines();
file.close()

grid = []
for line in lines:
    row = []
    for item in line:
        if item != "\n":
            row.append(item)

    grid.append(row)

def get_rocks():
    rock_positions = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "O":
                rock_positions.append((r,c))
    return rock_positions

def part_one():
    for r,c in get_rocks():
        q = deque([(r,c)])
        while q:
            cr, cc = q.popleft();
            for nr,nc in [(cr - 1, cc)]:
                if nr < 0 or nc < 0:
                    grid[cr][cc] = "O"
                    if(cr,cc) != (r,c):
                        grid[r][c] = "."
                    continue

                if grid[nr][nc] == "#":
                    grid[cr][cc] = "O"
                    if(cr,cc) != (r,c):
                        grid[r][c] = "."
                    continue

                if grid[nr][nc] == "O":
                    grid[cr][cc] = "O"
                    if(cr,cc) != (r,c):
                        grid[r][c] = "."
                    continue

                q.append((nr,nc))

    position = 100
    total = 0
    for row in grid:
        count  = 0
        for rock in row:
            if rock == "O":
                count += 1
        total += count * position
        position -= 1

    return total





print(part_one())
