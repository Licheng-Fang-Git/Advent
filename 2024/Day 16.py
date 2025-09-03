from collections import deque
import heapq

file_name = "../input"
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
    while pq:
        cost, r, c, dr, dc = heapq.heappop(pq)
        seen.add((r,c,dr,dc))
        if map[r][c] == 'E':
            return cost
        # clockwise (1,0) -- > (0,-1) (r,c) --> (-c,r)  (-1, 0) --> (0,1) (r,c) --> (c, -r)
        for new_cost, nr, nc, ndr, ndc in [(cost+1, r + dr, c + dc, dr, dc), (cost + 1000, r , c, -dc, dr), (cost + 1000, r, c, dc, -dr)]:
            if map[nr][nc] == "#":
                continue
            if (nr,nc,ndr,ndc) in seen:
                continue
            heapq.heappush(pq,(new_cost, nr, nc, ndr, ndc))

def part_two(map):
    r,c = find_start_position(map)
    pq = [(0,r,c,0,1)]
    lowest_cost = {(r,c,0,1) : 0}
    backtrack = {}
    best_cost = float('inf')
    end = False
    end_state = set()
    while pq and end is False:
        cost, r, c, dr, dc = heapq.heappop(pq)
        if cost > lowest_cost.get((r,c,dr,dc), float('inf')) : continue
        if map[r][c] == 'E':
            if cost > best_cost:
                end = True
                continue
            best_cost = cost
            end_state.add((r,c,dr,dc))
        for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c+ dc, dr, dc), (cost + 1001, r - dc, c + dr, -dc, dr), (cost + 1000, r+ dc, c-dr, dc, -dr)]:
            if map[nr][nc] == '#':
                continue
            lowest = lowest_cost.get((nr, nc, ndr, ndc), float('inf'))
            if new_cost > lowest: continue
            if new_cost < lowest:
                backtrack[(nr, nc, ndr, ndc)] =  set()
                lowest_cost[(nr,nc,ndr,ndc)] = new_cost

            backtrack[(nr, nc, ndr, ndc)].add((r,c,dr,dc))
            heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))

    tiles = breadth_fill(end_state, backtrack)
    return tiles


def breadth_fill(end_state, backtrack):
    state = deque(end_state)
    seen =  set(end_state)
    while state:
        key = state.popleft()
        for last in backtrack.get(key, []):
            if last in seen:
                continue
            seen.add(last)
            state.append(last)

    return len({(r,c) for r, c, _, _ in seen})

# part_one(map)
print(part_two(map))