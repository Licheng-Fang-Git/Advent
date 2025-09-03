file = open("../input").read()

grid = []
for line in file.split("\n"):
    one_row = []
    for letter in line:
        one_row.append(letter)
    grid.append(one_row)

for row in grid:
    print(row)

part_one = 0
def check_diagonal_down_right(r, c, string):
    global part_one
    if string == "XMAS":
        part_one += 1
        return
    for nr, nc in [(r+1, c+1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        if grid[nr][nc] == "XMAS"[len(string)]:
            check_diagonal_down_right(nr, nc, string + grid[nr][nc])
def check_diagonal_up_right(r, c, string):
    global part_one
    if string == "XMAS":
        part_one += 1
        return
    for nr, nc in [(r-1, c+1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        if grid[nr][nc] == "XMAS"[len(string)]:
            check_diagonal_up_right(nr, nc, string + grid[nr][nc])
def check_diagonal_down_left(r, c, string):
    global part_one
    if string == "XMAS":
        part_one += 1
        return
    for nr, nc in [(r+1, c-1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        if grid[nr][nc] == "XMAS"[len(string)]:
            check_diagonal_down_left(nr, nc, string + grid[nr][nc])
def check_diagonal_up_left(r, c, string):
    global part_one
    if string == "XMAS":
        part_one += 1
        return
    for nr, nc in [(r-1, c-1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        if grid[nr][nc] == "XMAS"[len(string)]:
            check_diagonal_up_left(nr, nc, string + grid[nr][nc])

def check_left(r, c, string):
    global part_one
    if string == "XMAS":
        part_one += 1
        return
    for nr, nc in [(r,c-1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        if grid[nr][nc] == "XMAS"[len(string)]:
            check_left(nr, nc, string + grid[nr][nc])


def check_right(r, c, string):
    global part_one
    if string == "XMAS":
        part_one += 1
        return
    for nr, nc in [(r,c+1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        if grid[nr][nc] == "XMAS"[len(string)]:
            check_right(nr, nc, string + grid[nr][nc])

def check_up(r, c, string):
    global part_one
    if string == "XMAS":
        part_one += 1
        return
    for nr, nc in [(r-1,c)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        if grid[nr][nc] == "XMAS"[len(string)]:
            check_up(nr, nc, string + grid[nr][nc])

def check_down(r, c, string):
    global part_one
    if string == "XMAS":
        part_one += 1
        return
    for nr, nc in [(r+1,c)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        if grid[nr][nc] == "XMAS"[len(string)]:
            check_down(nr, nc, string + grid[nr][nc])

for r_idx, array in enumerate(grid):
    for c_idx, letter in enumerate(array):
        if letter == "X":
            check_left(r_idx, c_idx, "X")
            check_right(r_idx, c_idx, "X")
            check_up(r_idx, c_idx, "X")
            check_down(r_idx, c_idx, "X")
            check_diagonal_up_left(r_idx, c_idx, "X")
            check_diagonal_down_left(r_idx, c_idx, "X")
            check_diagonal_up_right(r_idx, c_idx, "X")
            check_diagonal_down_right(r_idx, c_idx, "X")

print(part_one)

part_two = 0

for r in range(1,len(grid)-1):
    for c in range(1,len(grid[0])-1):
        if grid[r][c] != "A":
            continue
        corners = [grid[r-1][c-1], grid[r-1][c+1], grid[r+1][c+1], grid[r+1][c-1]]
        if "".join(corners) in ["MMSS", "MSSM", "SMMS", "SSMM"]:
            part_two += 1

print(part_two)