file = open("input").readlines()

grid = []
flashes = 0
for line in file:
    line = line.strip()
    one_row= []
    for item in line:
        one_row.append(int(item))
    grid.append(one_row)

for row in grid:
    print(row)
print()
def has_flash():
    for r in range(len(grid)):
        for c in range(len(grid[0])):
             if grid[r][c] >= 10:
                 return True
    return False

def solve_two_simultaneously():
    for row in grid:
        if not all( value == 0 for value in row):
            return False
    return True

def change():
    global flashes
    for r in range(len(grid)):
        for c in range(len(grid[0])):
             if grid[r][c] >= 10:
                 flashes += 1
                 grid[r][c] = 0
                 for nr, nc in [(r+1,c), (r-1,c), (r,c-1), (r,c+1), (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1)]:
                    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                        continue
                    if grid[nr][nc] == 0: continue
                    grid[nr][nc] += 1
    return False

def solve_one():
    global flashes
    steps = 0
    while not solve_two_simultaneously():
        steps += 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                grid[r][c] += 1
        while has_flash():
            change()
        if solve_two_simultaneously():
            return steps
    return flashes


print(solve_one())
print()
for row in grid:
    print(row)