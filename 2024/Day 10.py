import queue
from collections import deque

map = []
column = []
count = 0
with open("/Users/andyfang/PycharmProjects/Advent/venv/Input") as file:
    for line in file:
        column = []
        for number in line:
            if number != "\n":
                if number != ".":
                    column.append(int(number))
                else:
                    column.append(number)

        map.append(column)
        count += 1

trail_heads = []
row = len(map)
column = len(map[0])

for i in range(row):
    for j in range(column):
        if map[i][j] == 9:
            trail_heads.append((i, j))

print(trail_heads)

def score(grid, r, c):
    position = deque([(r, c)])
    visited = {()}
    score = 0
    while len(position) > 0:
        cr, cc = position.popleft()
        for nr, nc in [(cr - 1, cc), (cr, cc + 1), (cr + 1, cc), (cr, cc - 1)]:
            if nr < 0 or nc < 0 or nr >= len(map[0]) or nc >= len(map[0]):
                continue
            if grid[nr][nc] != grid[cr][cc] - 1:
                continue
            if grid[nr][nc] == 0:
                score += 1
            else:
                position.append((nr, nc))
        print(cr, cc)

    return score

total = 0
for i in trail_heads:
    total += score(map, i[0], i[1])

print(total)
