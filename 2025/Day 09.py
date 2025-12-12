import math

file = open("../input").read().split("\n")
print(file)
red_dots = []
for i in range(len(file)):
    c,r = map(int, file[i].split(","))
    red_dots.append((c,r))

def part_one():
    largest_area = 0
    for i in range(len(file)):
        x1,y1 = map(int, file[i].split(","))
        for j in range(len(file)):
            x2, y2 = map(int, file[j].split(","))
            largest_area =  max(largest_area, (abs(x2 - x1)+1) * (abs(y2 - y1)+1))

    return largest_area

def point_in_poly(x, y):
    inside = 0
    for (x1,y1),(x2,y2) in zip(red_dots, red_dots[1:] + red_dots[:1]):
        if (x == x1 == x2 and min(y1,y2) <= y <= max(y2,y1)) or (y == y1 == y2 and min(x1,x2) <= x <= max(x1,x2)):
            return True
        if (y1 < y < y2 or y2 < y < y1) and (x < (y - y1) * (x2 - x1) / (y2 - y1) + x1):
            inside += 1
    return inside % 2 != 0

def valid_square(x1,y1,x2,y2):
    x1,x2 = sorted([x1,x2])
    y1,y2 = sorted([y1,y2])
    for x,y in [(x1,y1), (x2,y2), (x1,y2), (x2,y1)]:
        if  not point_in_poly(x,y):
            return False
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if (x,y) in [(x1,y1), (x2,y2), (x1,y2), (x2,y1)]:
                continue
            if not point_in_poly(x,y):
                return False
    return True

print(point_in_poly(5,2))

def part_two():

    # this helps tell me the polygon is closed because the x and y's always have a matched value
    # for (x1,y1),(x2,y2) in zip(red_dots, red_dots[1:] + red_dots[:1]):
    #     assert (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2)

    largest_area = 0
    for i in range(len(file)):
        x1,y1 = map(int, file[i].split(","))
        for j in range(len(file)):
            x2, y2 = map(int, file[j].split(","))
            area = (abs(x2 - x1)+1) * (abs(y2 - y1)+1)
            if area > largest_area and valid_square(x1,y1, x2, y2):
                largest_area = area

    return largest_area




# 84859 84224 13619 17248
print(part_two())