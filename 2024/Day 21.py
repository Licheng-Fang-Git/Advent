from collections import deque
from functools import cache
from itertools import product

def compute(pad):
    pos = {}
    for r in range(len(pad)):
        for c in range(len(pad[0])):
            if pad[r][c] is not None:
                pos[pad[r][c]] = (r,c)

    seqs = {}
    for x in pos:
        for y in pos:
            if x == y:
                seqs[(x,y)] = "A"
                continue
            q = deque([(pos[x], "")])
            possible = []
            optimal =  float("inf")
            while q:
                (r,c), move = q.popleft()
                for nr, nc, nm in [(r - 1, c, "^"), (r + 1, c, "v"), (r , c -1 , "<"), (r, c + 1, ">")]:
                    if nr < 0 or nc < 0 or nr >= len(pad) or nc >= len(pad[0]):
                        continue
                    if pad[nr][nc] is None:
                        continue
                    if pad[nr][nc] == y:
                        if optimal < len(move)+1 : break
                        optimal = len(move)+1
                        possible.append(move + nm + "A")
                    else:
                        q.append(((nr, nc), move + nm))
                else:
                    continue
                break
            seqs[(x,y)] = possible
    return seqs

def compute_seqs(string, seqs):
    options = [seqs[(x,y)] for x,y in zip("A" + string, string)]
    return ["".join(x) for x in product(*options)]

keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]
num_seqs = compute(keypad)
direction_pad = [
    [None, "^", "A"],
    ["<", "v", ">"]
]
dir_seqs = compute(direction_pad)
dir_lengths = {key: len(value[0]) for key, value in dir_seqs.items()}
print(dir_lengths)

def part_one(code):
    total = 0
    robot1 = compute_seqs(code, num_seqs)
    next_robot = robot1
    for _ in range(2):
        possible_next = []
        for seq in next_robot:
            possible_next += compute_seqs(seq, dir_seqs)
        min_len =  min(map(len, possible_next))
        next_robot = [seq for seq in possible_next if len(seq) == min_len]
    total += len(next_robot[0]) * int(code[:-1])
    return total

@cache
def compute_lengths(x,y, depth=2):
    if depth == 1:
        print("depth 1:", x,y, dir_lengths[(x,y)])
        return dir_lengths[(x,y)]
    optimal = float("inf")
    for seq in dir_seqs[(x,y)]:
        print("Seq of", x,y, ":", seq)
        length = 0
        for a,b in zip("A" + seq, seq):
            print(a,b)
            length += compute_lengths(a,b,depth-1)
            print(length)
        optimal = min(optimal, length)
    return optimal

def part_two(code):
    inputs = compute_seqs(code, num_seqs)
    optimal =  float("inf")
    for seq in inputs:
        print("Sequence of robot1:", seq)
        length = 0
        for x,y in zip("A" + seq, seq):
            print(x,y)
            length += compute_lengths(x,y)
            print("final len:", length)
        optimal = min(optimal, length)
    print(optimal)

part_one_total = 0

lines = open("../input").readline()
print(lines)
part_two(lines)

# for line in lines:
#     part_one_total += part_one(line)
# print(part_one_total)

