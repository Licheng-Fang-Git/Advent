block1, block2 = open("input").read().split("\n\n")

rules = {}
for line in block1.split("\n"):
    rule = list(map(int, line.split("|")))
    x,y = rule[0], rule[1]
    if x not in rules:
        rules[x] = set()
    rules[x].add(y)

part_one = 0

for update in block2.split("\n"):
    update = list(map(int,update.split(",")))
    right_order = True
    for i in range(len(update)):
        for j in range(i, len(update)):
            if i == j: continue
            if update[i] in rules:
                if update[j] not in rules[update[i]]:
                    right_order = False
            else:
                right_order = False

    if right_order:
        part_one += update[len(update)//2]

print(part_one)
part_two = 0

for update in block2.split("\n"):
    update = list(map(int,update.split(",")))
    right_order = True
    for i in range(len(update)):
        for j in range(i, len(update)):
            if i == j: continue
            if update[i] in rules:
                if update[j] not in rules[update[i]]:
                    right_order = False
                    temp = update[i]
                    update[i] = update[j]
                    update[j] = temp
            else:
                right_order = False
                temp = update[i]
                update[i] = update[j]
                update[j] = temp

    if right_order is False:
        part_two += update[len(update)//2]

print(part_two)