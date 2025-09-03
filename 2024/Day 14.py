# import re
#
# WIDTH = 101 #101
# HEIGHT = 103 # 103
# robots = []
# with open("input") as file:
#     for line in file:
#         robots.append(tuple(map(int, re.findall(r"-?\d+", line))))
#
#
# finish = []
# for px, py, vx, vy in robots:
#     fy = (px + vx * 100) % WIDTH
#     fx = (py + vy * 100) % HEIGHT
#     finish.append((fx,fy))
#
# grid =[[0]*WIDTH for _ in range(HEIGHT)]
#
# for x,y in finish:
#     grid[x][y] += 1
#
# for row in grid:
#     print(row)
#
# def quadrantsCheck(finish):
#     tl= bl= tr= br = 0
#     horizontal_line = HEIGHT // 2 # 3
#     vertical_line = WIDTH // 2 # 5
#
#     for x, y in finish:
#         if x == horizontal_line and y == vertical_line :
#             continue
#         # quad 1
#         if x < horizontal_line and y < vertical_line:
#             tl += 1
#         # quad 2
#         if x < horizontal_line and y > vertical_line:
#             bl += 1
#         if x > horizontal_line and y < vertical_line:
#             tr += 1
#         if x > horizontal_line and y > vertical_line:
#             br += 1
#     return tl * tr * br * bl;
#
#
# print(quadrantsCheck(finish))

import re

WIDTH = 101
HEIGHT = 103

robots = []

for line in open(0):
    robots.append(tuple(map(int, re.findall(r"-?\d+", line))))

min_sf = float("inf")
best_iteration = None

for second in range(WIDTH * HEIGHT):
    result = []

    for px, py, vx, vy in robots:
        result.append(((px + vx * second) % WIDTH, (py + vy * second) % HEIGHT))

    tl = bl = tr = br = 0

    VM = (HEIGHT - 1) // 2
    HM = (WIDTH - 1) // 2

    for px, py in result:
        if px == HM or py == VM: continue
        if px < HM:
            if py < VM:
                tl += 1
            else:
                bl += 1
        else:
            if py < VM:
                tr += 1
            else:
                br += 1

    sf = tl * bl * tr * br

    if sf < min_sf:
        min_sf = sf
        best_iteration = second

print(best_iteration)