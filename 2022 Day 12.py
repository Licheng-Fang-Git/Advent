import heapq
from collections import deque

file = open("input").readlines()
map = []
sr,sc= 0,0
for i, line in enumerate(file):
    one_row = []
    for j, letter in enumerate(line.strip()):
        if letter == "S":
            sr,sc = i,j
        if letter == "E":
            er,ec = i,j
        one_row.append(letter)
    map.append(one_row)


alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_dic = {}
count = 0
for letter in alphabet:
    letter_dic[letter] = count
    count += 1
letter_dic["S"] = 0
letter_dic["E"] = letter_dic["z"]

print(letter_dic)
for row in map:
    print(row)

def solve_dfs(node, pos, visited):
    if node == "E":
        return len(visited)
    ans = float("inf")
    r,c = pos
    for nr, nc in [(r+1, c), (r-1,c), (r, c+1), (r, c-1)]:
        if nr < 0 or nc < 0 or nr >= len(map) or nc >= len(map[0]): continue
        if (nr,nc) in visited: continue
        if (letter_dic[map[nr][nc]] - letter_dic[node]) > 1: continue
        visited.add((nr,nc))
        ans = min(ans, solve_dfs(map[nr][nc], (nr,nc), visited))
        if ans != float("inf"): print(ans)
    return ans

def solve_one():
    pq = [(0, sr, sc)]
    seen = {( sr, sc)}
    while pq:
        print(pq)
        m, r, c = heapq.heappop(pq)
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr >= len(map) or nc >= len(map[0]): continue
            if (nr, nc) in seen: continue
            if (letter_dic[map[nr][nc]] - letter_dic[map[r][c]]) > 1: continue
            if map[nr][nc] == "E":
                return m + 1
            seen.add((nr, nc))
            heapq.heappush(pq, (m+1, nr, nc))

    return seen


# print(solve_one())
print(solve_dfs("S", (sr,sc), visited=set()))