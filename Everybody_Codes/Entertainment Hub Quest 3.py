block1, block2 = open('../input').read().split('\n\n')
file = block1.split('\n')
dice_num = {}
for dice in file:
    dice = dice.split(" ")
    die_num = int(dice[0][0])
    faces = list(map(int,dice[1][7:len(dice[1])-1].split(',')))
    seed = int(dice[2][5:])
    dice_num[die_num] = [faces,seed,seed,0,0,0]
grid = []
for row in block2.split("\n"):
    one_row = []
    for num in row:
        one_row.append(int(num))
    grid.append(one_row)

print(dice_num)
print(grid)

def part_one():
    total = 0
    roll_num = 1
    while total <= 10000:
        roll_points = 0
        for key in dice_num:
            seed = dice_num[key][1]
            pulse = dice_num[key][2]
            spin = roll_num * pulse
            result_idx = dice_num[key][3] + spin
            result = dice_num[key][0][result_idx%len(dice_num[key][0])]
            pulse = pulse + spin
            pulse = pulse % seed
            pulse = pulse + 1 + roll_num + seed
            dice_num[key][2] = pulse
            dice_num[key][3] = result_idx
            dice_num[key][4] = result
            roll_points += dice_num[key][4]
            print(key, roll_points, dice_num[key][4])

        total += roll_points
        roll_num += 1
    return roll_num

def part_two():
    race_checkpoints = list(map(int, list(block2)))
    total = 0
    roll_num = 1
    race_idx = 0
    race_result = []

    while len(race_result) < len(dice_num.keys()):
        print(race_result)
        for key in dice_num:
            if key in race_result:
                continue
            # if the dice num result meets all of the checkpoints
            if dice_num[key][5] == len(race_checkpoints):
                print(roll_num, key, dice_num[key][5])
                race_result.append(key)
                continue

            seed = dice_num[key][1]
            pulse = dice_num[key][2]
            spin = roll_num * pulse
            result_idx = dice_num[key][3] + spin
            result = dice_num[key][0][result_idx % len(dice_num[key][0])]
            pulse = pulse + spin
            pulse = pulse % seed
            pulse = pulse + 1 + roll_num + seed
            dice_num[key][2] = pulse
            dice_num[key][3] = result_idx
            dice_num[key][4] = result

            # get the checkpoint your at
            race_idx = dice_num[key][5]
            print(roll_num, key, race_idx)
            # check if the checkpoint is equal to your result
            if dice_num[key][4] == race_checkpoints[race_idx]:
                dice_num[key][5] += 1
        roll_num += 1
    return race_result

def roll(key, roll_num):
    seed = dice_num[key][1]
    pulse = dice_num[key][2]
    spin = roll_num * pulse
    result_idx = dice_num[key][3] + spin
    result = dice_num[key][0][result_idx % len(dice_num[key][0])]
    pulse = pulse + spin
    pulse = pulse % seed
    pulse = pulse + 1 + roll_num + seed
    dice_num[key][2] = pulse
    dice_num[key][3] = result_idx
    dice_num[key][4] = result
    return dice_num[key][4]

def part_three():
    agg_set = set()
    for key in dice_num:
        possible_set = set()
        roll_num = 1
        pos = roll(key, roll_num)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if pos == grid[i][j]:
                    possible_set.add((i, j))
        agg_set |= possible_set
        roll_num += 1
        while len(possible_set) > 0:
            pos = roll(key, roll_num)
            next_set = set()
            for r,c in possible_set:
                for nr, nc in [(r+1,c), (r-1,c), (r, c+1), (r, c-1), (r,c)]:
                    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                        continue
                    if grid[nr][nc] == pos:
                        next_set.add((nr,nc))

            possible_set = next_set
            agg_set |= possible_set
            roll_num += 1
    print(len(agg_set))

# print(part_one())
# part_two()

part_three()

