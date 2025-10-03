file = open("../input").read()

grid = []
directions = []
for line in file.split("\n"):
    one_row = []
    if 'R' in line:
        directions = line
        continue
    if not line:
        continue
    for idx, val in enumerate(line):
        if val == " ":
            one_row.append("-1")
        else:
            one_row.append(val)
    grid.append(one_row)

for row in grid:
    print(row)

print(directions)



def part_one():
    pos = 0
    numbers = []
    turn_signs = ['R']
    r, c = 0, grid[0].index(".")
    number = ""
    for val in directions:
        if val.isdigit():
            number += val
        else:
            turn_signs.append(val)
            numbers.append(int(number))
            number = ""
    numbers.append(int(directions[-1]))
    mr,mc = -1,0
    while numbers:
        move = numbers.pop(0)
        turn_sign = turn_signs.pop(0)
        print(move, turn_sign)
        #(0,1) -> R (1,0) L (-1,0)  (-1,0) -> R(0,1) L(0,-1)
        if turn_sign == "R":
            mr,mc = mc, mr * -1
        if turn_sign == "L":
            mr,mc = mc, mr
        print(mr, mc)
        for i in range(move):
            print(r,c)

            r += mr
            c += mc
            if c >= len(grid[0]):
                c_idx = c
                while grid[r][c_idx-1] != "-1" and c_idx - 1 >= 0:
                    c_idx -= 1
                if grid[r][c_idx] == "#":
                    break
                c = c_idx

            elif c < 0:
                c_idx = c
                while grid[r][c_idx + 1] != "-1":
                    c_idx += 1
                if grid[r][c_idx] == "#":
                    break
                c = c_idx

            elif r < 0:
                r_idx = r
                while grid[r_idx + 1][c] != "-1":
                    r_idx += 1
                if grid[r_idx][c] == "#":
                    break
                r = r_idx

            elif r >= len(grid):
                r_idx = r
                while grid[r_idx - 1][c] != "-1":
                    r_idx -= 1
                if grid[r_idx][c] == "#":
                    break
                r = r_idx

            if grid[r][c] == "#":
                r -= mr
                c -= mc
                break

    return r,c
part_one()