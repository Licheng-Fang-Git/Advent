from collections import deque
file = open("../input").read().split("\n")
pixel_map = [[file[i][j] for j in range(len(file[0]))] for i in range(len(file))]
triangle_dir = {}
sr,sc = 0,0
er,ec = 0,0
def part_one():
    global sr,sc,er,ec
    pairs = []
    downwards_tri = True
    for i in range(len(pixel_map)):
        downwards_tri = True
        for j in range(len(pixel_map[0])):
            if pixel_map[i][j] == 'S':
                sr,sc = i,j
                triangle_dir[(i, j)] = downwards_tri
            elif pixel_map[i][j] == 'E':
                er,ec = i,j
                triangle_dir[(i, j)] = downwards_tri
            if pixel_map[i][j] == '.':
                continue
            if pixel_map[i][j] != 'T':
                downwards_tri = not downwards_tri
                continue
            if downwards_tri:
                for nr, nc in [(i,j+1), (i,j-1), (i-1,j)]:
                    if nr < 0 or nc < 0 or  nr >= len(pixel_map) or nc >= len(pixel_map[0]):
                        continue
                    if [(i,j),(nr,nc)] in pairs or [(nr,nc),(i,j)] in pairs:
                        continue
                    if pixel_map[nr][nc] == "T":
                        pairs.append([(i,j),(nr,nc)])
            else:
                for nr, nc in [(i,j+1), (i,j-1), (i+1,j)]:
                    if nr < 0 or nc < 0 or  nr >= len(pixel_map) or nc >= len(pixel_map[0]):
                        continue
                    if [(i,j),(nr,nc)] in pairs or [(nr,nc),(i,j)] in pairs:
                        continue
                    if pixel_map[nr][nc] == "T":
                        pairs.append([(i,j),(nr,nc)])
            triangle_dir[(i, j)] = downwards_tri
            downwards_tri = not downwards_tri
    return len(pairs)

def part_two():
    global sr,sc,er,ec
    dq = deque([(sr,sc,0)])
    visited = set()
    while dq:
        r,c,j = dq.popleft()
        if triangle_dir[(r,c)]:
            for nr, nc in [(r, c + 1), (r, c - 1), (r - 1, c)]:
                if nr < 0 or nc < 0 or nr >= len(pixel_map) or nc >= len(pixel_map[0]):
                    continue
                if pixel_map[nr][nc] == "E":
                    return j + 1
                if (nr,nc) in visited:
                    continue
                if pixel_map[nr][nc] == "T":
                    dq.append((nr,nc,j+1))
                    visited.add((nr,nc))
        else:
            for nr, nc in [(r, c + 1), (r, c - 1), (r + 1, c)]:
                if nr < 0 or nc < 0 or nr >= len(pixel_map) or nc >= len(pixel_map[0]):
                    continue
                if pixel_map[nr][nc] == "E":
                    return j + 1
                if (nr,nc) in visited:
                    continue
                if pixel_map[nr][nc] == "T":
                    dq.append((nr,nc,j+1))
                    visited.add((nr,nc))

def part_three():
    pass
part_one()
part_two()