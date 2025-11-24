from collections import deque

file = open("../input").read().split("\n")

grid = []
one_row = []
for row in file:
    one_row = []
    for val in row:
        one_row.append(val)
    grid.append(one_row)

def part_one_bfs(r,c, visited):
    er,ec = len(grid)-1, len(grid[0])-1
    dq = deque([(r,c)])
    visited.add((r,c))
    count = 1
    while dq:
        r,c  = dq.popleft()
        for nr, nc in [(r-1, c), (r+1,c), (r,c+1), (r,c-1)]:
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                continue
            if (nr, nc) in visited:
                continue
            if grid[r][c] >= grid[nr][nc]:
                count += 1
                dq.append((nr,nc))
                visited.add((nr,nc))
    return [count, visited]

def part_three_bfs(starting_points):
    er,ec = len(grid)-1, len(grid[0])-1
    dq = deque([])
    visited = set()
    for sr, sc in starting_points:
        dq.append((sr,sc))
        visited.add((sr,sc))
    count = 1
    while dq:
        r,c  = dq.popleft()
        for nr, nc in [(r-1, c), (r+1,c), (r,c+1), (r,c-1)]:
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                continue
            if (nr, nc) in visited:
                continue
            if grid[r][c] >= grid[nr][nc]:
                count += 1
                dq.append((nr,nc))
                visited.add((nr,nc))
    return count

dic = {}
max_barr = 0
first_max_barr_info = []
first_explodes = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        dic[(i,j)] = part_one_bfs(i, j, set())
        if dic[(i,j)][0] > max_barr:
            max_barr = dic[(i,j)][0]
            first_max_barr_info = [(i,j), dic[(i,j)][1], max_barr]

print(first_max_barr_info)
# max_barr = 0
# sec_max_bar_info = []
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if (i,j) == first_max_barr_info[0]:
#             continue
#         dic[(i,j)] = part_one_bfs(i,j, first_max_barr_info[1].copy())
#         if dic[(i,j)][0] > max_barr:
#             max_barr = dic[(i,j)][0]
#             sec_max_bar_info = [(i,j), dic[(i,j)][1].copy(), max_barr]
#
# max_barr = 0
# third_max_bar_info = []
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if (i,j) == first_max_barr_info[0] or (i,j) == sec_max_bar_info[0]:
#             continue
#         if (i,j) in sec_max_bar_info[1]:
#             continue
#         dic[(i,j)] = part_one_bfs(i,j, sec_max_bar_info[1].copy())
#         if dic[(i,j)][0] > max_barr:
#             max_barr = dic[(i,j)][0]
#             third_max_bar_info = [(i,j), dic[(i,j)][1].copy(), max_barr]
#
#
# sp = []
# if first_max_barr_info:
#     sp.append(first_max_barr_info[0])
# if sec_max_bar_info:
#     sp.append(sec_max_bar_info[0])
# if third_max_bar_info[0] != ():
#     sp.append(third_max_bar_info[0])

# print(sp)
# print(sum([first_max_barr_info[2], sec_max_bar_info[2], third_max_bar_info[2]]))
# print(part_three_bfs(sp))

