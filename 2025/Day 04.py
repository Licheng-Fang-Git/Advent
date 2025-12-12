file = open("../input").read().split("\n")
total_removed = 0
grid = [ [file[i][j] for j in range(len(file[0]))] for i in range(len(file))]

def neighbors(x,y):
    count = 0
    for nr, nc in [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)]:
        if nr < 0 or nc < 0 or nr >= len(file) or nc >= len(file[0]):
            continue
        if grid[nr][nc] == "@":
            count += 1
    return count
def part_one():
    global total_removed
    total = 0
    remove = set()
    for r in range(len(file)):
        for c in range(len(file[0])):
            if grid[r][c] == "@" and neighbors(r,c) < 4:
                total += 1
                remove.add((r,c))
    print(remove)
    for r,c in remove:
        grid[r][c] = "."
    total_removed += total
    return total

def part_two():
    while part_one() >= 1:
        print(total_removed)

part_two()