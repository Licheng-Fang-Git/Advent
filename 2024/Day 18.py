import re
from collections import deque

f = open('../input')
data = []
for lines in f:
    data.append(lines.rstrip())

s = 70
grid = [[0]*(s+1) for  i in range(s+1)]

def part_one(n):
    global data
    for line in data[:n]:
        line = line.split(",")
        cr,cc = map(int,line)
        grid[cc][cr] = 1

    q = deque([(0,0,0)])
    seen = {(0, 0)}

    while q:
        r, c, d = q.popleft()
        for nr,nc in [(r + 1, c), (r, c + 1 ), (r-1,c), (r, c-1)]:
            if nr < 0 or nc < 0 or nr > s or nc > s:
                continue
            if grid[nr][nc] == 1:
                continue
            if nr == nc == s:
                return True, d + 1
            if (nr,nc) in seen:
                continue
            seen.add((nr,nc))
            q.append((nr,nc,d+1))

    return False, -1

def part_two_whole_corrupted():
    global data
    go = part_one(0)[0]
    position = 2589
    while go is True:
        position += 1
        go = part_one(position)[0]
    return position;


# print(part_one(2994))
print(part_two_whole_corrupted())
print(data[2994])
