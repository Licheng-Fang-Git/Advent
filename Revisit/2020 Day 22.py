block1, block2 = open("../input").read().split("\n\n")

player1 = []
player2 = []

for line in block1.split("\n")[1:]:
    player1.append(line.strip())
for line in block2.split("\n")[1:]:
    player2.append(line.strip())

player1 = list(map(int, player1))
player2 = list(map(int, player2))

rounds = 0
while player1 and player2:
    rounds += 1
    ply1 = player1.pop(0)
    ply2 = player2.pop(0)
    if ply1 > ply2:
        player1.append(ply1)
        player1.append(ply2)
    else:
        player2.append(ply2)
        player2.append(ply1)

total_one = 0
if player2:
    for idx in range(len(player2)-1,-1,-1):
        total_one += player2[idx] * (len(player2)-idx)
else:
    for idx in range(len(player1) - 1, -1, -1):
        total_one += player1[idx] * (len(player1) - idx)

print(total_one)

