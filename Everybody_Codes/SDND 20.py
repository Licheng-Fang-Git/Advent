file = open("../input").read().split("\n")
downwards_tri = True
pixel_map = [ [file[i][j] for j in range(len(file[0]))] for i in range(len(file))]
pairs = []
for i in range(len(pixel_map)):
    downwards_tri = True
    for j in range(len(pixel_map[0])):
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
                    print(i,j,nr,nc)
                    pairs.append([(i,j),(nr,nc)])
        else:
            for nr, nc in [(i,j+1), (i,j-1), (i+1,j)]:
                if nr < 0 or nc < 0 or  nr >= len(pixel_map) or nc >= len(pixel_map[0]):
                    continue
                if [(i,j),(nr,nc)] in pairs or [(nr,nc),(i,j)] in pairs:
                    continue
                if pixel_map[nr][nc] == "T":
                    print(i,j,nr,nc)
                    pairs.append([(i,j),(nr,nc)])

        downwards_tri = not downwards_tri

for row in pixel_map:
    print(row)

print(len(pairs))