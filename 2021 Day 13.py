block1, block2 = open("input").read().split("\n\n")

points =  set()
instructions = []

for line in block1.split("\n"):
    x,y = line.split(",")
    points.add(complex(int(x),int(y)))

for line in block2.split("\n"):
    equation, number = line.split("=")
    if equation[-1] == "y":
        instructions.append(complex(0,int(number)))
    else:
        instructions.append(int(number))


def change_points(line_number, set_points):
    visible_set = set()
    if isinstance(line_number, complex) is True:
        for point in set_points:
            if point.imag < line_number.imag:
                visible_set.add(point)
                continue
            difference = line_number.imag - int(point.imag - line_number.imag)
            new_point = point.real + complex(0,difference)
            visible_set.add(new_point)
    else:
        for point in set_points:
            if point.real < line_number:
                visible_set.add(point)
                continue
            difference = line_number - int(point.real - line_number)
            new_point = difference + complex(0, point.imag)
            visible_set.add(new_point)


    return visible_set

def solve_one():
    new_points = points
    for instruction in instructions:

        new_points = change_points(instruction, {*new_points})
    return new_points


dots = solve_one()
print("Part One:", len(dots))

print(dots)
row = 0 + 1
col = 0 + 1
for dot in dots:
    if dot.real > col:
        col = dot.real
    if dot.imag > row:
        row = dot.imag
print(row, col)

answer = ""
for i in range(int(row)+1):
    answer += "\n"
    for j in range(int(col)+1):
        if (complex(j,i)) in dots:
            answer += "x "
        else:
            answer += "  "
print(answer)



# for point in points:
#     print(point.imag)

