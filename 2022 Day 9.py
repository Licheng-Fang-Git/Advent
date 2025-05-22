file = open("input").readlines()



rules = {
    "R" : 1,
    "U" : -1j,
    "L" : -1,
    "D" : 1j
}
visited = set()
head = 2 - 1j
tail = 1 - 2j

def dig_adjacent(tail_check):
    for next in [1, -1, 1j, -1j]:
        if next + tail_check == head:
            return False
    return True

def not_adjacent(tail_check):
    for next_spot in [1, -1, 1j, -1j, -1 + 1j, -1-1j, 1+1j, 1-1j]:
        if next_spot + tail_check == head:
            return False
    return True

def solve_one(direct, move_unit):
    global head, tail
    for _ in range(move_unit):
        print(head, tail)
        visited.add(tail)
        prev_head = head
        head += rules[direct]
        if not_adjacent(tail):
            if tail.real != head.real and tail.imag != head.imag:
                tail = prev_head
            else:
                tail += rules[direct]
        else:
            continue

for line in file:
    direction, units = line.split(" ")
    solve_one(direction, int(units))

print(len(visited))