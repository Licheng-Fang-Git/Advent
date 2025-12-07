from collections import deque
from functools import cache

file = open("../input").read().split("\n")
grid = [ [file[i][j] for j in range(len(file[i]))] for i in range(len(file))]
s = [(i,j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == "S"]

def solve_one():
    sr,sc = s[0]
    positions = deque([(sr,sc)])
    split_count = set()
    while positions:
        r,c = positions.popleft()
        for nr, nc in [(r+1,c)]:
            if nr >= len(grid):
                continue
            if grid[nr][nc] == "^":
                split_count.add((nr,nc))
                if (nr,nc - 1) not in positions:
                    positions.append((nr, nc - 1))
                if (nr, nc + 1) not in positions:
                    positions.append((nr, nc + 1))
            else:
                positions.append((nr,nc))
    return len(split_count)

@cache
def solve_two_dfs(position):
    if position[0] >= len(grid):
        return 1
    count = 0
    r,c = position
    print(r,c)
    if grid[r][c] != "^":
        count += solve_two_dfs((r+1,c))
    else:
        if grid[r][c] == "^":
            for nr,nc in [(r+1,c-1), (r+1,c+1)]:
                count += solve_two_dfs((nr,nc))
    return count

# solve_one()
print(solve_two_dfs(s[0]))
