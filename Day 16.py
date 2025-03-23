import heapq

file_name = "input"
file = open(file_name)
lines = file.readlines()
file.close()
map = []
for line in lines:
    one_row = []
    for item in line:
        if item != '\n':
            one_row.append(item)
    map.append(one_row)

for row in map:
    print(row)

def find_start_position(map):
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == 'S':
                sr, sc = r,c
                return sr,sc

def find_end_position(map):
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == "E":
                er, ec = r, c
                return er, ec

def part_one(map):
    r, c = find_start_position(map)
    pq = [(0, r , c, 0, 1)]
    seen = {(r, c, 0, 1)}
    end = False
    while pq and end is False:
        cost, r, c, dr, dc = heapq.heappop(pq)
        seen.add((r,c,dr,dc))
        if map[r][c] == 'E':
            print(cost)
            end = True
        # clockwise (1,0) -- > (0,-1) (r,c) --> (-c,r)  (-1, 0) --> (0,1) (r,c) --> (c, -r)
        for new_cost, nr, nc, ndr, ndc in [(cost+1, r + dr, c + dc, dr, dc), (cost + 1000, r , c, -dc, dr), (cost + 1000, r, c, dc, -dr)]:
            if map[nr][nc] == "#":
                continue
            if (nr,nc,ndr,ndc) in seen:
                continue
            heapq.heappush(pq,(new_cost, nr, nc, ndr, ndc))

part_one(map)