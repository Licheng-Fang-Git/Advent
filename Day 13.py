import re

file_name = "input"
file = open(file_name)
lines = file.read()
file.close()

total = 0
for line in lines.split("\n\n"):
    ax, ay, bx, by, px, py = map(int,re.findall(r"\d+", line))
    px += 10000000000000
    py += 10000000000000
    ca = ((px *  by) - (py * bx)) / ((ax * by) - (ay*bx))
    cb = (px - ax * ca) / bx

    if ca % 1 == 0 and cb % 1 == 0:
        total += ca * 3 + cb

print(total)