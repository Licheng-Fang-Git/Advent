file = open("input").read().split("\n\n")
monkeys= {}
for line in file:
    line = line.strip().split("\n")
    monkey_num = int(line[0].split(" ")[1][-2])
    monkeys[monkey_num] = []
    items = list(map(int, line[1].split(":")[1].replace(" ", "").split(",")))
    monkeys[monkey_num].append(items)
    operation = line[2].split("=")[1][-4:]
    monkeys[monkey_num].append(operation)
    test = "% " + line[3].split(" ")[-1]
    monkeys[monkey_num].append(test)
    if_true = line[4].split(" ")[-1]
    if_false = line[5].split(" ")[-1]
    monkeys[monkey_num].append(int(if_true))
    monkeys[monkey_num].append(int(if_false))
    monkeys[monkey_num].append(0)

print(monkeys)

# num = "5"
# equ = "* 19"
# print(eval(num + equ))

def solve_one():
    for monkey in monkeys:
        for item in monkeys[monkey][0]:
            monkeys[monkey][5] += 1
            if monkeys[monkey][1] == " old":
                worry_level = int(eval(str(item) + "*" + str(item)))
            else:
                worry_level = int(eval(str(item) + monkeys[monkey][1]))
            if int(eval(str(worry_level) + monkeys[monkey][2])) == 0:
                mky_num = monkeys[monkey][3]
                monkeys[mky_num][0].append(worry_level)
            else:
                mky_num = monkeys[monkey][4]
                monkeys[mky_num][0].append(worry_level)
        monkeys[monkey][0].clear()


for _ in range(10000):
    solve_one()

inspected_array = []
for monkey in monkeys:
    inspected_array.append(monkeys[monkey][5])
print(inspected_array)
max_val = max(inspected_array)
inspected_array.remove(max_val)
second_max_val = max(inspected_array)
total = max_val * second_max_val
print(total)
