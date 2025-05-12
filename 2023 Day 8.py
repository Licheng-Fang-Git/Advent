import sys
sys.setrecursionlimit(5000000)

instruction, file = open("input").read().split("\n\n")

connect = {}
for line in file.split("\n"):
    node, networks = line.split("=")
    first_net, second_net = networks[2:len(networks)-1].split(",")
    connect[node[:len(node)-1]] = [first_net, second_net[1:]]


def solve_steps(connections, original_ins, instructions, current_node, steps):

    if current_node[-1] == "Z":
        return steps

    if instructions == "":
        instructions = original_ins

    total = 0

    if instructions[0] == "L":
        total = solve_steps(connections, original_ins, instructions[1:], connections[current_node][0], steps + 1 )

    if instructions[0] == "R":
        total = solve_steps(connections, original_ins, instructions[1:], connections[current_node][1], steps + 1)

    return total



each_step = []
for node in connect.keys():
    if node[-1] == "A":
        each_step.append(solve_steps(connect, instruction, instruction, node, 0))


total_step = 0
for i, x in enumerate(each_step):
    for y in each_step[i:]:
        total_step += x*y

print(total_step)