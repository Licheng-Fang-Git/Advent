file = open("../input").readlines()
locations = [(0,0,0)]
prev_start = -1
def part_one(prev_s, next_start, n_open, n_height, prev_loc):
    new_locations = set()
    for i in range(prev_s+1,next_start+1):
        new_locations = set()
        for x, y, f in prev_loc:
            if x == start and (n_open + height < y or y < n_open):
                continue
            if y - 1 > 0:
                new_locations.add((x + 1, y - 1, f))
            new_locations.add((x + 1, y + 1, f+1))
        prev_loc = new_locations.copy()
    return new_locations

for triplet in file:
    start, opening, height = map(int,triplet.split(","))
    locations = part_one(prev_start, start,opening-1,height,locations)
    prev_start = start
    print(locations)


