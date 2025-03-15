import re

file_name = "input"
file = open(file_name)
lines = file.readlines()
file.close()

for line in lines:
    ax, ay = map(int,re.findall(r"\d+", line))
    print(ax, ay )

