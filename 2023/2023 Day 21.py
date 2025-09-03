import queue
from collections import deque

file = open("../input").readlines()

garden = []
for line in file:
    one_row = []
    for character in line.strip():
        one_row += character
    garden.append(one_row)


for row in garden:
    print(row)

def get_start():
    for r in range(len(garden)):
        for c in range(len(garden)):
            if garden[r][c] == "S":
                return r,c

sr,sc = get_start()
dq = deque([(sr,sc)])
for _ in range(64):
    LEN_DQ = len(dq)
    for _ in range(LEN_DQ):
        r,c = dq.popleft()
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr >= len(garden) or nc >= len(garden[0]): continue
            if garden[nr][nc] == "#": continue
            if (nr,nc) in dq: continue
            dq.append((nr,nc))

print(dq)
print(len(dq))