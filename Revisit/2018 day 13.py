file = open("../input").read()

track = []
carts = set()
x = 0
for line in file.split("\n"):
    one_row = []
    y=0
    for char in line:
        if char == "":
            one_row.append(".")
        elif char in "<>^v":
            carts.add((x,y,0))
            one_row.append(char)
        else:
            one_row.append(char)
        y += 1
    track.append(one_row)
    one_row = []
    x += 1
print(carts)

intersection_dir = {
    "left" : (0,-1),
    "right" : (0,1),
    "straight" : (0,0)
}
path_dic = {
    ">" : (0,1),
    "<" : (0,-1),
    "^" : (-1,0),
    "v" : (1,0)
}
switch_dic = {
    (0,1) : ">",
    (0,-1) : "<",
    (-1,0) : "^",
    (1,0) : "v"
}

for row in track:
    print(row)

for cart in carts:
    r,c = cart
    x,y = path_dic[track[r][c]]
    cart_sym = track[r][c]
    if track[r+x][c+y] == "\\":
        x,y = y,x
    elif track[r+x][c+y] == "/":
        x,y = y,-x
    else:
        pass