file = open("../input").readlines()
points = [(0,0), ]

directions = {
    "0" : "R",
    "1" : "D",
    "2" : "L",
    "3" : "U",
    "R" : (0, 1),
    "D" : (1, 0),
    "L" : (0, -1),
    "U" : (-1, 0)
}
r,c = 0,0
b = 0
for line in file:
    _, _, color = line.split()
    color = color[2:len(color)-1]
    dir = directions[color[-1]]
    dr, dc = directions[dir]
    n = int(color[:len(color)-1], 16)
    b += n
    r += dr * n
    c += dc * n
    points.append((r,c))

# xn(yn-1 + yn+1)
A = 1/2 * abs(sum([points[i][0] * (points[i-1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points))]))

i = A - b / 2 + 1 # inteior
i = i + b # exterior or the boundaries

print(i)

