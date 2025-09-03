import heapq

file = open("../input").read().split("\n")

grid = []

for index, line in enumerate(file):
    one_row = []
    for item in line:
        if index == 0: continue
        if item == "#": continue
        if item == "E":continue
        if index == 26:
            continue
        one_row.append(item)
    if one_row:
        grid.append(one_row)

for row in grid:
    print(row)

blizzard_pos = {">": set([]), "<": set([]), "v": set([]), "^": set([])}

expedition_pos = []
for r, row in enumerate(grid):
    for c, bliz in enumerate(row):
        if bliz == ".": continue
        if bliz == "E": expedition_pos.append((r, c))
        if bliz == ">": blizzard_pos[bliz].add((r, c))
        if bliz == "<": blizzard_pos[bliz].add((r, c))
        if bliz == "v": blizzard_pos[bliz].add((r, c))
        if bliz == "^": blizzard_pos[bliz].add((r, c))


row = len(grid)
col = len(grid[0])

def check_move(step, position):
    for x in blizzard_pos:
        for y in blizzard_pos[x]:
            rp, cp = y
            if x == ">":
                cp += step
                if (rp, cp % col) == position:
                    return False
            if x == "<":
                cp -= step
                if (rp, cp % col) == position:
                    return False
            if x == "v":
                rp += step
                if (rp % row,cp) == position:
                    return False
            if x == "^":
                rp -= step
                if (rp % row, cp) == position:
                    return False

    return True


def solve_one():
    steps = 0
    cr,cc = -1,0
    pq = [(0,cr,cc)]
    count = 0
    seen = {(0, cr, cc)}
    while pq:
        steps, cr, cc = heapq.heappop(pq)
        count += 1
        for nr, nc in [(cr+1, cc), (cr-1, cc), (cr, cc+1), (cr, cc-1)]:
            if (nr,nc) == (row-1,col):
                return steps + 1
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                continue
            if (steps, nr, nc) in seen: continue
            seen.add((steps, nr, nc))
            if check_move(steps+1, (nr,nc)):
                heapq.heappush(pq, (steps+1, nr, nc))
            else:
                if check_move(steps+1, (cr,cc)):

                    heapq.heappush(pq, (steps+1, cr,cc))
        # if count == 23:
        #     break
    return steps

print("Part One: ", solve_one())
# print("check")
print(check_move(3, (4,3)))