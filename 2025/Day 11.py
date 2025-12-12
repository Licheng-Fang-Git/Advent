from functools import cache
file = open("../input").read().splitlines()
connections = {}

for line in file:
    device, out = line.split(": ")
    outputs = out.split(" ")
    connections[device] = outputs

def dfs_solve_one(node, dest ):
    if dest == node:
        return 1
    count = 0
    for neighbor in connections[node]:
        count += dfs_solve_one(neighbor, dest)
    return count

#bitmasking
@cache
def dfs_solve_two(node, visited_mask):
    print(node, visited_mask)
    if node == "dac":
        visited_mask |= 1
    if node == "fft":
        visited_mask |= 2
    if node == "out":
        return 1 if visited_mask == 3 else 0
    if node not in connections: return 0
    count = 0
    for neighbor in connections[node]:
        count += dfs_solve_two(neighbor, visited_mask)
    return count

print(dfs_solve_two("svr", 0))

# 0 --> 000
# 1 --> 001
# 2 --> 010
# 3 --> 011

# 000 dac |= 1 --> 001
# 001 fft |= 2 --> 011 --> 3
# 000 fft |= 2 --> 010
# 010 dac |= 1 --> 011 --> 3