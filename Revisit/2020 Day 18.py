file = open("../input").readlines()

def extract(idx):
    paren_stack = []
    op_paren_stack = []
    while line[idx] != ")":
        item = line[idx]
        if item == "(":
            idx, item = extract(idx+1)
        if not paren_stack :
            paren_stack.append(item)
            idx += 1
            continue
        if item.isdigit():
            paren_stack.append(str(eval(paren_stack.pop() + op_paren_stack.pop() + item)))
        else:
            op_paren_stack.append(item)
        idx += 1
    return idx, paren_stack.pop()

def solve_one():
    solve_stack = []
    op_stack = []
    i = 0
    while i < len(stack):
        value = stack[i]
        if not solve_stack:
            solve_stack.append(value)
            i += 1
            continue
        if value.isdigit():
            solve_stack.append(str(eval(solve_stack.pop() + op_stack.pop() + value)))
        else:
            op_stack.append(value)
        i += 1
    return solve_stack.pop()


total_one = 0
for line in file:
    line = line.replace(" ", "")
    stack = []
    i = 0
    while i < len(line):
        value = line[i]
        if value == "(":
            i, value = extract(i+1)
            stack.append(value)
        elif value != ")":
            stack.append(value)
        i += 1
    total_one += int(solve_one())
print(total_one)