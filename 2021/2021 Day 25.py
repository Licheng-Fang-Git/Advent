file = open("../input").readlines()

grid = []
for line in file:
    line = line.strip()
    one_row = []
    for item in line:
        one_row.append(item)
    grid.append(one_row)

for row in grid:
    print(row)

print()
def move_east(east_cucumbers):
    can_move = False
    old_grid = [row[:] for row in grid]
    for cucumber in east_cucumbers:
        cr,cc = cucumber
        if grid[cr][(cc + 1) % len(grid[0])] in ">v" or old_grid[cr][(cc + 1) % len(grid[0])] in ">v" :
            continue
        else:
            grid[cr][(cc + 1) % len(grid[0])] = ">"
            grid[cr][cc] = "."
            can_move = True

    return can_move

def move_west(west_cucumbers):
    can_move = False
    old_grid = [row[:] for row in grid]
    for cucumber in west_cucumbers:
        cr, cc = cucumber
        if grid[(cr +  1) % len(grid)][cc] in ">v" or old_grid[(cr +  1) % len(grid)][cc] == "v":
            continue
        else:
            grid[(cr + 1) % len(grid)][cc] = "v"
            grid[cr][cc] = "."
            can_move = True

    return can_move

def solve_one():
    can_move = True
    steps = 0
    while can_move:
        steps += 1
        east_dir = []
        west_dir = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] == ">":
                    east_dir.append((r, c))
                if grid[r][c] =="v":
                    west_dir.append((r, c))
        east = move_east(east_dir)
        west = move_west(west_dir)

        if east or west:
            continue
        else:
            can_move = False
    return steps

print(solve_one())