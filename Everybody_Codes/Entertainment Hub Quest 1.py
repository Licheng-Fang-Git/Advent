import numpy as np
block1, block2 = open("../input").read().split("\n\n")

machine = []

for line in block1.split("\n"):
    one_row = []
    for val in line.strip():
        one_row.append(val)
    machine.append(one_row)
# machine.append(['.' for _ in range(len(machine[0]))])

directions = block2.split("\n")
# for idx, row in enumerate(directions):
#     directions[idx] += row[-1]

dic = {
    'R' : [1,1],
    'L' : [1, -1]
}

def part_one():
    m = len(machine)
    n = len(machine[0])
    final_slots = {}
    fs = 1
    for i in range(n):
        if i % 2 == 0:
            final_slots[i] = fs
            fs += 1
    total = 0
    toss_slot = 1
    for i in range(0, n, 2):
        fs = final_slots[play_game(0, i, directions[toss_slot - 1])]
        if (fs*2) - toss_slot <= -1:
            total += 0
        else:
            total += (fs*2) - toss_slot
        toss_slot += 1
    return total
def part_two():
    m = len(machine)
    n = len(machine[0])
    final_slots = {}
    fs = 1
    for i in range(n):
        if i % 2 == 0:
            final_slots[i] = fs
            fs += 1
    print(final_slots)
    total = 0
    max_token_slot = 0
    toss_slot = 0
    for token in directions:
        max_token_slot = 0
        one_slot_total = 0
        for i in range(0, n, 2):
            max_token_slot = max(max_token_slot, one_slot_total)
            one_slot_total = 0
            toss_slot = final_slots[i]
            fs = final_slots[play_game(0, i, token)]
            if (fs * 2) - toss_slot <= -1:
                one_slot_total += 0
            else:
                one_slot_total += (fs * 2) - toss_slot

            if one_slot_total > max_token_slot:
                # print(toss_slot, one_slot_total)
                max_token_slot = one_slot_total

        total += max_token_slot
        print(token, max_token_slot)

    return total

def part_three():
    m = len(machine)
    n = len(machine[0])
    final_slots = {}
    fs = 1
    for i in range(n):
        if i % 2 == 0:
            final_slots[i] = fs
            fs += 1

    total = 0
    max_token_slot = 0
    toss_slot = 0
    token_dictionary = {}
    for token in directions:
        token_dictionary[token] = []
        toss_slot = 1
        for i in range(0, n, 2):
            one_slot_total = 0
            fs = final_slots[play_game(0,i, token)]
            if (fs * 2) - toss_slot <= -1:
                one_slot_total += 0
            else:
                one_slot_total += (fs * 2) - toss_slot
            toss_slot += 1
            token_dictionary[token].append(one_slot_total)

    dp = [ -1 for _ in range(7)]
    print(token_dictionary)
    token_slot_vales = [
        token_dictionary[key] for key in token_dictionary]


    for row in token_slot_vales:
        print(row)




def play_game(sr,sc, direction_row):
    cr, cc = sr, sc
    dirct_idx = 0
    while len(machine) > cr >= 0 and dirct_idx < len(direction_row):
        if direction_row[dirct_idx] == "R":
            if cc + dic['R'][1] >= len(machine[0]):
                cr = cr + dic['L'][0]
                cc = cc + dic['L'][1]
            else:
                cr = cr + dic['R'][0]
                cc = cc + dic['R'][1]

        elif direction_row[dirct_idx] == 'L':
            if cc + dic['L'][1] < 0 :
                cr = cr + dic['R'][0]
                cc = cc + dic['R'][1]
            else:
                cr = cr + dic['L'][0]
                cc = cc + dic['L'][1]

        while cr < len(machine) and machine[cr][cc] != '*':
                cr += 1
        dirct_idx += 1
    return cc



# print(part_one())

# print(part_two())

part_three()
