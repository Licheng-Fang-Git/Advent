from functools import cache
file = open("../input").read().split("\n")
grid = [["." for j in range(40)] for i in range(6)]

@cache
def solve_one(cycles):
    cycle = 1
    instruction_position = 0
    x = 1
    skip = False
    while cycle < cycles:
        if file[instruction_position] == "noop":
            cycle += 1
            instruction_position += 1
            continue
        if skip:
            number = file[instruction_position].split(" ")[1]
            cycle += 1
            instruction_position += 1
            x += int(number)
            skip = False
            continue

        if "addx" in file[instruction_position] and skip is not True:
            skip = True
            cycle += 1
    return x

def sprite_pos(pos_x):
    pr, pc = pos_x
    return [(pr, pc - 1), (pr, pc), (pr, pc + 1)]

@cache
def solve_two(r, c, cycles, instr_num, prev_x):
    cycle = 1
    instruction_position = instr_num
    x = prev_x
    skip = False
    pr, pc = r,c
    sprite_position = prev_x + 1
    three_sprite_pixels = sprite_pos((pr, sprite_position))
    while cycle < cycles:
        pc += 1
        print(three_sprite_pixels, x)
        if file[instruction_position] == "noop":
            cycle += 1
            instruction_position += 1
            grid[pr][pc] = "."
            continue

        if skip:
            number = file[instruction_position].split(" ")[1]
            cycle += 1
            instruction_position += 1
            if (pr, pc) in three_sprite_pixels:
                grid[pr][pc] = "#"
            else:
                grid[pr][pc] = "."
            x += int(number)
            sprite_position = x
            three_sprite_pixels = sprite_pos((pr, sprite_position))
            skip = False
            continue

        if "addx" in file[instruction_position] and skip is not True:
            skip = True
            cycle += 1
            if (pr, pc) in three_sprite_pixels:
                grid[pr][pc] = "#"
            else:
                grid[pr][pc] = "."

    return instruction_position, x

array = [20, 60, 100, 140, 180, 220]
total_part_one = 0


# for signal in array:
#     print(signal, solve_one(signal))
#     total_part_one += signal * int(solve_one(signal))

# next_instruct, pre_x = solve_two(0,-1, 39, 0, 1)
# print(next_instruct)
print(solve_one(39))
next_instruct, pre_x =  solve_two(1,-1, 39, 19, solve_one(39))
# solve_two(2,-1, 39, 0)
# solve_two(3,-1, 159)
# solve_two(1,-1, 79)

print()

for row in grid:
    for character in row:
        print(character, end="")
    print(end="\n")