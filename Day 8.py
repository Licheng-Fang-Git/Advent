file = open("input").readlines()

grid =  []
for line in file:
    one_row = []
    line = line.strip()
    for value in line:
        one_row.append(value)
    grid.append(one_row)

for row in grid:
    print(row)

antennas = {}

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == ".": continue
        if grid[r][c] not in antennas: antennas[grid[r][c]] = []
        antennas[grid[r][c]].append((r,c))

ans_node = []

for array in antennas.values():
    for i in range(len(array)):
        for j in range(i, len(array)):
            r1, c1 = array[i]
            r2, c2 = array[j]
            ans_node.append((abs(r1 - r2), abs(c1 - c2)))
            ans_node.append((abs(r1 + r2), abs(c1 + c2)))

print(ans_node)


