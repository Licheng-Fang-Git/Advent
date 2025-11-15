file = open("../input").read().split("\n")
grid = []
star_loc = {}

for i in range(len(file)):
    one_row = []
    for j in range(len(file[i])):
        if file[i][j] == "*":
            star_loc[str(i)+"|"+str(j)] = []
        one_row.append(file[i][j])
    grid.append(one_row)

N,M = len(grid), len(grid[0])

def check_for_symbol(r,c):
    for nr,nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1), (r+1,c+1), (r+1,c-1), (r-1,c-1), (r-1,c+1)]:
        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            continue
        if not grid[nr][nc].isdigit() and grid[nr][nc] != ".":
            return True
    return False

def check_for_star(r,c):

    for nr,nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1), (r+1,c+1), (r+1,c-1), (r-1,c-1), (r-1,c+1)]:
        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            continue
        if grid[nr][nc] == "*":
            return list(map(str, [nr,nc]))
    return []

def part_one():
    ans = 0
    adjacent_num = False
    num = ""
    for i in range(N):
        if num.isdigit() and adjacent_num:
            ans += int(num)
        num = ""
        adjacent_num = False
        for j in range(M):
            if grid[i][j].isdigit():
                num += grid[i][j]
                if check_for_symbol(i,j):
                    adjacent_num = True

            elif not grid[i][j].isdigit():
                if adjacent_num and num != "":
                    ans += int(num)
                    adjacent_num = False
                    num = ""
                else:
                    num = ""
    return ans

def part_two():
    ans = 0
    adjacent_num = False
    num = ["", []]
    for i in range(N):
        if num[0].isdigit() and adjacent_num:
            for pos in num[1]:
                star_loc[pos[0] +"|"+pos[1]].append(int(num[0]))
        num = ["", []]
        adjacent_num = False
        for j in range(M):
            if grid[i][j].isdigit():
                num[0] += grid[i][j]
                loc_asterix = check_for_star(i,j)
                if loc_asterix:
                    adjacent_num = True
                    if loc_asterix not in num[1]:
                        num[1].append(loc_asterix)

            elif not grid[i][j].isdigit():
                if adjacent_num and num != "":
                    for pos in num[1]:
                        star_loc[pos[0]+"|"+pos[1]].append(int(num[0]))
                    adjacent_num = False
                    num = ["", []]
                else:
                    num = ["", []]
    for key in star_loc:
        if len(star_loc[key]) >= 2:
            print(star_loc[key])
            ans += star_loc[key][0] * star_loc[key][1]
    return ans

print(part_two())





