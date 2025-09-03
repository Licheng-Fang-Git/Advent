
file = open("../input").readlines()


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
        return 1
    total = 0
    for neighbor in conn[node]:
        if neighbor == "Start":
            continue
        if neighbor.islower() and neighbor in req:
            if no_more is True:
                continue
            total += search(neighbor, [*req, neighbor], True)
        else:
            total += search(neighbor, [*req, neighbor], no_more)


    return total

print(search("Start", ["Start"], False))

# nums = {1, 2, 3, 4, 1}
#
# hello = [(nums[i],nums[j]) for i in range(len(nums)) for j in range(i,len(nums))]
# print(hello)

nums =  [1,2,3,4]

new_nums = nums[:]
new_nums.append(5)
print(new_nums)


