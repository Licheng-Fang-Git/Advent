from collections import deque

file = 1358
grid = [[ 0 for _ in range(50)] for _ in range(50)]


def wall(x,y):
    sum_point = x*x + 3*x + 2*x*y + y + y*y + 1358
    sum_point = bin(sum_point)
    count  = 0
    idx = sum_point.find('b')
    for bit in sum_point[idx+1:]:
        if bit == '1':
            count += 1
    return count % 2 == 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if wall(j,i):
            grid[i][j] = '.'
        else:
            grid[i][j] = '#'


def bfs():
    dq = deque([(1,1,0)])
    seen = {(1, 1)}
    end = (39,31)
    while dq:
        x,y,m = dq.popleft()
        if m+1 > 50:
            print(x,y)
            return len(seen)
        for nr, nc in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                continue
            if grid[nr][nc] == '#':
                continue
            if (nr, nc) == end:
                return m+1
            if (nr,nc) in seen:
                continue
            seen.add((nr,nc))
            dq.append((nr,nc,m+1))
print(bfs())