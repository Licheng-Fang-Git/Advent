import sys
file = open("input").readlines()

sys.setrecursionlimit(3000)

edges = [line.strip().split("-") for line in file]
conn = {}
for x,y in edges:
    if x == "start":
        x = "Start"
    if y == "start":
        y = "Start"
    if x == "end":
        x = "End"
    if y == "end":
        y = "End"
    if x not in conn: conn[x] = set()
    if y not in conn: conn[y] = set()
    conn[x].add(y)
    conn[y].add(x)

sets = set()
print(conn)

def search(node, req, no_more):
    if node == "End":
        print(req)
        sets.add(tuple(req))
        return

    if node.islower():
        if node in req:
            if no_more is True:
                return
            no_more = True

    for neighbor in conn[node]:
        if neighbor == "Start":
            continue
        new_req = req[:]
        new_req.append(neighbor)
        search(neighbor, new_req, no_more)

search("Start", ["Start"], False)

# nums = {1, 2, 3, 4, 1}
#
# hello = [(nums[i],nums[j]) for i in range(len(nums)) for j in range(i,len(nums))]
# print(hello)

nums =  [1,2,3,4]

new_nums = nums[:]
new_nums.append(5)
print(new_nums)

print(len(sets))

