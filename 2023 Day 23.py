file =  open("input").readlines()
grid = []

for row in file:
    one_row = []
    for character in row.strip():
        one_row.append(character)
    grid.append(one_row)

def get_start():
    global grid
    sr, sc = 0, grid[0].index(".")
    return sr,sc
def get_end():
    global grid
    er, ec = len(grid) - 1, grid[len(grid) - 1].index(".")
    return er,ec

def find_neighbors():
    global grid
    points = []
    sr, sc = 0, grid[0].index(".")
    er, ec = len(grid) - 1, grid[len(grid) - 1].index(".")
    points.append((sr, sc))
    points.append((er, ec))
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#": continue
            neighbor = 0
            for nr,nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]): continue
                if grid[nr][nc] == "#": continue
                neighbor += 1
            if neighbor >= 3:
                points.append((r,c))
    return points

points = find_neighbors()

def graph_pts(points,grid):

    dirs = {
        "^" : [(-1,0),(1,0),(0,-1),(0,1)],
        "v" : [(-1,0),(1,0),(0,-1),(0,1)],
        ">" : [(-1,0),(1,0),(0,-1),(0,1)],
        "<" : [(-1,0),(1,0),(0,-1),(0,1)],
        "." : [(-1,0),(1,0),(0,-1),(0,1)]
    }

    graph = { pts: {} for pts in points }
    for sr,sc in graph:
        stack = [(0, sr, sc)]
        seen = {(sr, sc)}
        while stack:
            n, r, c = stack.pop()
            if n != 0 and (r,c) in points:
                graph[(sr,sc)][(r,c)] = n
                continue
            for dr, dc in dirs[grid[r][c]]:
                nr = r + dr
                nc =  c + dc
                if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                    continue
                if grid[nr][nc] == "#":
                    continue
                if (nr, nc) in seen:
                    continue
                seen.add((nr,nc))
                stack.append((n + 1 , nr , nc))
    return graph

graph = graph_pts(points, grid)
print(graph)

seen = set()
def dfs(pt):
    global graph
    if pt == get_end():
        return 0
    m = -float("inf")
    seen.add(pt)
    for nm in graph[pt]:
        if nm not in seen:
            m =  max(m, dfs(nm) + graph[pt][nm])
    seen.remove(pt)
    return m


print(dfs(get_start()))
