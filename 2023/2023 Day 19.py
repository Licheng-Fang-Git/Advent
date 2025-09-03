block1, block2 = open("../input").read().split("\n\n")

work_flows = {}
items = {}

for line in block1.split("\n"):
    line = line[0:len(line)-1]
    name, rules = line.split("{")
    rules = rules.split(",")
    fallback = rules[-1]
    work_flows[name] = ([], fallback )
    for rule in rules[:-1]:
        compare_rule, flow = rule.split(":")
        key_one = compare_rule[0] # a,m
        cmp_sign_one = compare_rule[1]
        value_one = compare_rule[2:]
        work_flows[name][0].append((key_one, cmp_sign_one, value_one, flow))

ops = {
    ">" : int.__gt__,
    "<" : int.__lt__
}

def accept(item, wkf):
    if wkf == "A":
        return True
    if wkf == "R":
        return False

    comparisons, fall_back = work_flows[wkf]
    for compare in comparisons:
        key, cmp_sign, value, next_flow = compare
        if ops[cmp_sign](int(item[key]), int(value)):
            return accept(item, next_flow)

    return accept(item, fall_back)

total = 0
for line in block2.split():
    line =  line[1:len(line)-1].split(",")
    for r in line:
        items[r[0]] = r[2:]

    if accept(items, "in"):
        for item_value in items.values():
            total += int(item_value)

print(total)




