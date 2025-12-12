file = open("input").read().split("\n")
curr_dial = 50
ans = 0
for rotate in file:
    if rotate[0] == "L":
        for i in range((curr_dial - int(rotate[1:]))+1, curr_dial) :
            if i % 100  == 0:
                ans += 1
        curr_dial = (curr_dial - int(rotate[1:])) % 100
    elif rotate[0] == "R":
        for i in range(curr_dial+1, (curr_dial + int(rotate[1:]))) :
            if i % 100 == 0:
                ans += 1
        curr_dial = (curr_dial + int(rotate[1:])) % 100
    if curr_dial == 0:
        ans += 1
print(ans)
