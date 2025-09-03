from operator import truediv

file = open("../input").readlines()

grid = []
for line in file:
    one_row = []
    for character in line:
        if character != "\n":
            one_row.append(character)
    grid.append(one_row)

part_two_grid = grid

def guard_position():
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "^":
                return x,y

def in_bounds(r,c):
    if r < 0  or c < 0 or r >= len(grid) or c >= len(grid[0]):
        return False
    return True

def part_one(grid, r, c):
    sr,sc = r,c
    dr,dc = -1,0
    visited =  set()
    while True:
        visited.add((sr, sc, dr, dc))
        for nr,nc in [(sr + dr, sc + dc)]:
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                return False
            if grid[nr][nc] == "#":
                dr, dc = dc, dr * -1
            else:
                sr, sc = nr,nc

            if (sr,sc,dr,dc) in visited:
                return True
    return visited

def part_two(grid):
    count = 0
    gr,gc = guard_position()
    for cr in range(len(grid)):
        for cc in range(len(grid[0])):
            print(cr,cc)
            if grid[cr][cc] != ".": continue
            grid[cr][cc] = "#"
            if part_one(grid, gr, gc):
                count += 1
            grid[cr][cc] = "."
    return count

print(part_two(grid))
# print(len(part_one(grid)))