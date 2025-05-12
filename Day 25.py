file = open("input").read().split("\n\n")

locks = []
keys = []

def two_d(array):
    maps = []
    for i_row in array.split():
        row = []
        for item in i_row:
            row.append(item)
        maps.append(row)
    return maps

for line in file:
    grid = two_d(line)
    # lock
    if all( x == "#" for x in grid[0]):
        lock_value = []
        for c in range(len(grid[0])):
            count  = 0
            for r in range(len(grid)):
                if grid[r][c] == "#":
                    count += 1
            lock_value.append(count)
        locks.append(tuple(lock_value))
    else:
        key_value = []
        for c in range(len(grid[0])):
            count  = 0
            for r in range(len(grid)):
                if grid[r][c] == "#":
                    count += 1
            key_value.append(count)
        keys.append(tuple(key_value))

can_fit_count = 0
for lock in locks:
    for key in keys:
        overlap = False
        for i in range(5):
            fit_difference = 7 - lock[i]
            if key[i] <= fit_difference:
                continue
            else:
                overlap = True
        if overlap:
            can_fit_count += 0
        else:
            can_fit_count += 1

print(can_fit_count)



