from functools import cache

file = open("input").read()
stones = list(map(int, file.strip().split(" ")))
print(stones)

def solve_one():
    for _ in range(75):
        output = []
        for stone in stones:
            if stone == 0:
                output.append(1)
                continue
            string = str(stone)
            length = len(string)
            if length % 2 == 0:
                output.append(int(string[:length // 2]))
                output.append(int(string[length // 2:]))
            else:
                output.append(stone * 2024)
        stones = output

@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps - 1)
    string = str(stone)
    length = len(string)
    if length % 2 == 0:
        return count(int(string[:length // 2]), steps - 1) + count(int(string[length // 2:]), steps - 1)
    return count(stone * 2024, steps - 1)

print(sum(count(stone, 75) for stone in stones))
