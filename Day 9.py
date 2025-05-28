import heapq
file = open("input").read()

memory = []
file_num = 0
heaps_with_free_space = [[] for _ in range(10)]
for j, num in enumerate(file):
    if j % 2 == 0:
        for _ in range(int(num)):
            memory.append(file_num)
        file_num += 1
    else:
        heapq.heappush(heaps_with_free_space[int(num)], len(memory))
        for _ in range(int(num)):
            memory.append(-1)


blanks = [idx for idx, free in enumerate(memory) if free == -1]
heaps_with_free_space[0].clear()

# def solve_one():
#     idx = len(memory) - 1
#     while idx >= 0:
#         if memory[idx] == -1:
#             while memory[-1] == -1:
#                 memory.pop()
#                 idx -= 1
#             continue
#         check_free = 0
#         while memory[check_free] != -1 and check_free + 1 < len(memory):
#             check_free += 1
#         if check_free + 1 == len(memory):
#             break
#         else:
#             memory[check_free] = memory[idx]
#             memory.pop()
#             idx -= 1

def solve_one():
    print(blanks)
    for idx, blank in enumerate(blanks):
        if blank >= len(memory): continue
        last_num = memory[-1]
        while last_num == -1:
            memory.pop()
            last_num = memory[-1]
        memory[blank] = last_num
        memory.pop()

def solve_two():
    i = len(memory) - 1
    while i >= 0:
        if memory[i] == -1:
            i -= 1
            continue
        file_id = memory[i]
        file_width = 0
        while i >= 0 and file_id == memory[i]:
            file_width += 1
            i -= 1
        smallest_idx = float("inf")
        best_width = 0
        for j in range(file_width, 10):
            if heaps_with_free_space[j] and j != 0:
                if heaps_with_free_space[j][0] < smallest_idx:
                    smallest_idx = heaps_with_free_space[j][0]
                    best_width = j
        if smallest_idx == float("inf"): continue
        if smallest_idx > i: continue
        heapq.heappop(heaps_with_free_space[best_width])
        if memory[smallest_idx + file_width] == -1:
            heapq.heappush(heaps_with_free_space[best_width - file_width], smallest_idx + file_width)

        for j in range(file_width):
            memory[smallest_idx + j] = file_id
            memory[i + j + 1] = -1
    return memory


solve_two()

total = 0
for idx, num in enumerate(memory):
    if num == -1:
        num = 0
    total += idx * num

print(total)