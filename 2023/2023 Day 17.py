import heapq
from collections import deque

file = open("../input").readlines()
grid = []
for line in file:
    line = line.strip()
    one_row = []
    for num in line:
        one_row.append(int(num))
    grid.append(one_row)

for row in grid:
    print(row)



def part_one(grid):
    pq = ([(0,0,0,0,1,0)])
    seen =  set()
    while pq:
        hl, r, c, dr, dc, n = heapq.heappop(pq)
        
        if (r,c,dr,dc,n) in seen:
            continue
        seen.add((r,c,dr,dc,n))

        if (r,c) == (len(grid)-1, len(grid[0])-1) and n >= 4:
            return hl

        if n < 10 and (dr,dc) != (0,0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heapq.heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

        if n >= 4 and (dr,dc) != (0,0):
            for ndr, ndc in [(-1,0), (1,0), (0,1), (0,-1)]:
                if (ndr,ndc) != (-dr, -dc) and (dr, dc) != (ndr, ndc):
                    nr = r + ndr
                    nc = c + ndc
                    if  0 <= nr < len(grid) and 0 <= nc < len(grid[0]) :
                        heapq.heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))




print(part_one(grid))
