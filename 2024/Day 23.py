import setuptools.command.alias

file = open("../input")

egdes = [line.strip().split("-") for line in file]

conn = {}

for x,y in egdes:
    if x not in conn: conn[x] = set()
    if y not in conn: conn[y] = set()
    conn[x].add(y)
    conn[y].add(x)

inter_connected = set()
for x in conn:
    for y in conn[x]:
        for z in conn[y]:
            if x != z and x in conn[z]:
                three_connections =  tuple(sorted([x,y,z]))
                inter_connected.add(three_connections)
t_start = set()
for sets in inter_connected:
    for cn in sets:
        if cn[0:1] == "t":
            t_start.add(sets)

seen = set()
def search(node, req):
    key = tuple(sorted(req))
    if key in seen:
        return
    seen.add(key)
    for neighbor in conn[node]:
        if neighbor in req: continue
        if not all(neighbor in conn[query] for query in req ): continue
        search(neighbor, [*req, neighbor])


for x in conn:
    search(x, [x])

max_len = max(map(len, seen))
longest = [",".join(sorted(s)) for s in seen if len(s) == max_len]
print(longest)