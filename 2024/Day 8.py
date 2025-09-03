from compileall import compile_dir

file = open("../input").readlines()

grid =  []
for line in file:
    one_row = []
    line = line.strip()
    for value in line:
        one_row.append(value)
    grid.append(one_row)


antennas = {}
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == ".": continue
        if grid[r][c] not in antennas: antennas[grid[r][c]] = []
        antennas[grid[r][c]].append((r,c))

ans_node = set()
def solve_one(array, k):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if i == j: continue
            r1, c1 = array[i]
            r2, c2 = array[j]
            if c1 > c2:
                ans_node.add((r1 + k * abs(r2-r1), c1 - k * abs(c2-c1)))
                ans_node.add((r2 - k * abs(r2-r1), c2 + k * abs(c2-c1)))
            else:
                ans_node.add((r1 + k * abs(r2 - r1), c1 + k * abs(c2 - c1)))
                ans_node.add((r2 - k * abs(r2 - r1), c2 - k * abs(c2 - c1)))

def solve_two(array, k):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if i == j: continue
            r1, c1 = array[i]
            r2, c2 = array[j]
            cr1, cc1 = 0, 0
            cr2, cc2 = 0,0
            k = 0
            while 0 <= cr1 < len(grid) and 0 <= cc1 < len(grid[0]):
                if c1 > c2:
                    cr1, cc1 = (r1 + k * abs(r2-r1), c1 - k * abs(c2-c1))
                    ans_node.add((cr1, cc1))

                else:
                    cr1 = r1 + k * abs(r2-r1)
                    cc1 = c1 + k * abs(c2-c1)
                    ans_node.add((cr1, cc1))
                k += 1
            k = 0
            while 0 <= cr2 <= len(grid) and 0 <= cc2 <= len(grid[0]):
                if c1 > c2:
                    cr2, cc2 = r2 - k * abs(r2 - r1), c2 + k * abs(c2 - c1)
                    ans_node.add((cr2, cc2))
                else:
                    cr2, cc2 = r2 - k * abs(r2 - r1), c2 - k * abs(c2 - c1)
                    ans_node.add((cr2, cc2))
                k += 1

for array in antennas.values():
    solve_two(array, 0)

ans = [(r,c) for r,c in ans_node if 0 <= r < len(grid) and 0 <= c < len(grid[0])]
print(ans)
for r,c in ans:
    grid[r][c] = "#"
for row in grid:
    print(row)
print(len(ans))


