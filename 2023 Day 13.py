file = open("input").read().split("\n\n")

grid = []


def mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        total_changes = 0
        for x, y in zip(above, below):
            for a, b in zip(x, y):
                if a != b:
                    total_changes += 1

        if total_changes == 1:
            return r
    return 0


total = 0
for line in file:
    grid = line.split()
    total += mirror(grid) * 100
    vertical_grid = list(zip(*grid))
    # for row in grid:
    #     one_row = []
    #     for c in row:
    #         one_row += c
    #     column_grid.append(one_row)
    # vertical_grid = []
    # for c in range(len(column_grid[0])):
    #     one_row = ""
    #     for r in range(len(column_grid)):
    #         one_row += grid[r][c]
    #     vertical_grid.append(one_row)

    total += mirror(vertical_grid)

print(total)
