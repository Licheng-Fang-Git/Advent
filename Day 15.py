from collections import deque

file_name = "input"
file = open(file_name)
lines = file.readlines()
file.close()
part_one_grid = []
part_two_grid = []
part_two_grid_row = []
instructions = ""

for line in lines:
    if "#" in line:
        part_two_grid_row = []
        for element in line:
            if element == '#':
                part_two_grid_row.append('#')
                part_two_grid_row.append('#')
            if element == 'O':
                part_two_grid_row.append('[')
                part_two_grid_row.append(']')
            if element == '.':
                part_two_grid_row.append('.')
                part_two_grid_row.append('.')
            if element == '@':
                part_two_grid_row.append('@')
                part_two_grid_row.append('.')
        part_two_grid.append(part_two_grid_row)
        part_one_grid.append([ letter for letter in line if letter != '\n'])

    if "<" in line:
        instructions += line


def start_position(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                return r,c

def get_next_move(move):
    DIRECTIONS = {"^" : (-1, 0),
                  ">" : (0,+1),
                  "<" : (0, -1),
                  "v" : (+1,0)}

    return DIRECTIONS[move]

def get_gps(grid):
    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "[":
                total += 100 * r + c
    return total

def part_one(part_one_grid):
    for move in instructions:
        if move == "\n":
            continue
        r,c = start_position(part_one_grid)
        targets = [(r,c)]
        go = True
        dot = False
        cr, cc = r,c
        dr, dc = get_next_move(move)
        while go is True and dot is False:
            cr += dr
            cc += dc
            if part_one_grid[cr][cc] == '#':
                go = False
            if part_one_grid[cr][cc] == 'O':
                targets.append((cr,cc))
            if part_one_grid[cr][cc] == '.':
                dot = True

        if go is False:
            continue

        for br, bc in targets[1:]:
            part_one_grid[br + dr][bc + dc] = "O"


        part_one_grid[r][c] = "."
        part_one_grid[r + dr][c + dc] = "@"

def part_two(part_two_grid):
    for move in instructions:
        if move == "\n":
            continue
        r, c = start_position(part_two_grid)
        dr, dc = get_next_move(move)
        go, move_items =  move_blocks(move, r, c)
        if go is False:
            continue
        for br, bc in move_items[::-1]:
            if part_two_grid[br][bc] == '@':
                part_two_grid[br+dr][bc+dc] = part_two_grid[br][bc]
                part_two_grid[br][bc] = '.'
            else:
                part_two_grid[br + dr ][bc + dc] = part_two_grid[br][bc]
                part_two_grid[br][bc] = '.'
    return part_two_grid

def move_blocks(move, r, c):
    dr, dc = get_next_move(move)
    dq = deque([(r,c)])
    seen = set([])
    items_move = [(r, c)]

    while dq:
        nr, nc = dq.popleft()
        nr += dr
        nc += dc
        if part_two_grid[nr][nc] == '#':
            return False, []
        if (nr,nc) in seen:
            continue
        seen.add((nr,nc))
        if part_two_grid[nr][nc] == "[":
            if not((nr, nc) in items_move):
                items_move.append((nr,nc))
            if not((nr, nc + 1) in items_move):
                items_move.append((nr,nc+1))
            dq.append((nr,nc))
            dq.append((nr,nc+1))

        if part_two_grid[nr][nc] == "]":
            if not((nr, nc) in items_move):
                items_move.append((nr,nc))
            if not((nr, nc - 1) in items_move):
                items_move.append((nr,nc-1))
            dq.append((nr,nc))
            dq.append((nr,nc-1))

    return True, items_move

part_one(part_one_grid)
one_answer = get_gps(part_one_grid)
part_two(part_two_grid)
two_answer= get_gps(part_two_grid)
print(two_answer)
