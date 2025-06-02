file = open("input")
lines = file.readlines()
file.close()

grid = []
for line in lines:
    row = []
    for item in line:
        if item != "\n":
            row.append(item)

    grid.append(row)

distances = [[-1] * (len(grid[0])) for i in range(len(grid))]

def get_start():
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                return r,c

def part_one():
    global distances, grid
    r,c = get_start()
    distances[r][c] = 0
    while grid[r][c] != 'E':
        for nr, nc in [(r - 1, c), (r, c + 1), (r, c - 1), (r +1, c)]:
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                continue
            if grid[nr][nc] == '#':
                continue
            if distances[nr][nc] != -1:
                continue
            distances[nr][nc] = distances[r][c] + 1
            r = nr
            c = nc

    count = 0
    for r in range(len(distances)):
        for c in range(len(distances[0])):
            if grid[r][c] == "#" : continue
            for nr, nc  in [(r + 2, c), (r - 1, c + 1), (r, c + 2), (r + 1, c + 1)]:
                if nr < 0 or nc < 0 or nr >= len(distances) or nc >= len(distances): continue
                if grid[nr][nc] == "#": continue
                if abs(distances[r][c] - distances[nr][nc]) == 6: count += 1

    return count

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            break
    else:
        continue
    break

dists = [[-1] * cols for _ in range(rows)]
dists[r][c] = 0

while grid[r][c] != "E":
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
        if grid[nr][nc] == "#": continue
        if dists[nr][nc] != -1: continue
        dists[nr][nc] = dists[r][c] + 1
        r = nr
        c = nc

count = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "#": continue
        for radius in range(2, 21):
            for dr in range(radius + 1):
                dc = radius - dr
                for nr, nc in {(r + dr, c + dc), (r + dr, c - dc), (r - dr, c + dc), (r - dr, c - dc)}:
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                    if grid[nr][nc] == "#": continue
                    if dists[r][c] - dists[nr][nc] >= 100 + radius: count += 1

print(count)

