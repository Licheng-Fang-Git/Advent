import re

WIDTH = 101 #101
HEIGHT = 103 # 103
robots = []
with open("input") as file:
    for line in file:
        robots.append(tuple(map(int, re.findall(r"-?\d+", line))))


finish = []
for px, py, vx, vy in robots:
    fy = (px + vx * 100) % WIDTH;
    fx = (py + vy * 100) % HEIGHT;
    finish.append((fx,fy))

grid =[[0]*WIDTH for _ in range(HEIGHT)]

for x,y in finish:
    grid[x][y] += 1

for row in grid:
    print(row)

def quadrantsCheck(finish):
    tl= bl= tr= br = 0
    horizontal_line = HEIGHT // 2 # 3
    vertical_line = WIDTH // 2 # 5

    for x, y in finish:
        if x == horizontal_line and y == vertical_line :
            continue
        # quad 1
        if x < horizontal_line and y < vertical_line:
            tl += 1
        # quad 2
        if x < horizontal_line and y > vertical_line:
            bl += 1
        if x > horizontal_line and y < vertical_line:
            tr += 1
        if x > horizontal_line and y > vertical_line:
            br += 1
    return tl * tr * br * bl;


print(quadrantsCheck(finish))
