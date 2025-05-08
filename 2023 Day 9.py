file = open("input").read().split("\n")

def part_one(array):
    if all(n == 0 for n in array):
        return array[0]
    difference = []
    for x,y in zip(array[:-1], array[1:]):
        difference.append(x-y)
    return array[0] + part_one(difference)

total = 0
for line in file:
    line = list(map(int,line.split()))

    total += part_one(line)
print(total)

