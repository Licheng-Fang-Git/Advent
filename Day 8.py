from compileall import compile_dir

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

ans_node = set()

for array in antennas.values():
    for i in range(len(array)):
        for j in range(i, len(array)):
            if i == j: continue
            r1, c1 = array[i]
            r2, c2 = array[j]
            ans_node.add((r1 - abs(r2-r1), c1 - abs(c2-c1)))
            ans_node.add((r2 - abs(r2-r1), c2 - abs(c2-c1)))


print(ans_node)
print(len(grid), len(grid[0]))
ans_node = [ (r,c) for r,c in ans_node if 0 <= r < len(grid) and 0 <= c < len(grid[0])]
print(ans_node)
for r,c in ans_node:
    grid[r][c] = "#"
for row in grid:
    print(row)
print(len(ans_node))


