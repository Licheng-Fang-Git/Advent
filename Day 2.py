file = open("aoc_input").readlines()
#968
#561

def inc_or_dec(cx, cy):
    if cx > cy:
        return -1
    if cx < cy:
        return 1
    return 0

def solve_one(row):
    flow = inc_or_dec(row[0], row[1])
    count = 0
    if flow == 0: count += 1
    for x,y in zip(row, row[1:]):
        #x,y
        #76
        if flow < 0:
            if x < y:
                count += 1
            if x-y < 1 or x-y > 3:
                count += 1
        # x,y
        #12
        if flow > 0:
            if x > y:
                count += 1
            if y-x < 1 or y-x > 3:
                count += 1

    return count
def solve_two(fail_count, row):
    if fail_count == 0:
        return True
    fail_counts = []
    for each_idx in range(len(row)):
        updated_row = [num for i, num in enumerate(row) if i != each_idx]
        fail_counts.append(solve_one(updated_row))

    if 0 in fail_counts:
        return True
    else:
        return False

total = 0
for line in file:
    line  = line.strip().split(" ")
    print(line)
    if solve_two(solve_one(list(map(int, line))), list(map(int,line))):
        total += 1



print(total)