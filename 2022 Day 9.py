file = open("input").readlines()

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

rules = {
    "R" : 1 + 0j,
    "U" : 0 + -1j,
    "L" : -1 + 0j,
    "D" : 0 + 1j
}
visited = set()
head = 0 + 0j
tail = 0 + 0j

def not_adjacent(tail_check, head_check):
    print("Check: ", head_check, tail_check)
    if abs(head_check - tail_check) > 1 :
        print("distance:", abs(tail_check + head_check))
        return True
    return False

def solve_one(direct, move_unit):
    global head, tail
    for _ in range(move_unit):
        visited.add(tail)
        head += rules[direct]
        print(head, tail)
        offset = head - tail
        print("offset", offset, offset.real**2 + offset.imag**2 )
        if offset.real**2 + offset.imag**2 > 2:
            print(complex(sign(offset.real), sign(offset.imag)))
            tail = tail + complex(sign(offset.real), sign(offset.imag))
            visited.add(tail)

for line in file:
    direction, units = line.split(" ")
    solve_one(direction, int(units))

print(len(visited))