file = open("../input").read().split("\n")

# print(10000000000000/ (file[0]/file[-1]))
rotations = 0
ans = 0
print(file)
for i in range(1,len(file)-1):
    if "|" in file[i-1]:
        vl = file[i-1].find("|")
        prev = int(file[i-1][vl+1:])
    else:
        prev = int(file[i-1])

    if "|" in file[i]:
        vl = file[i].find("|")
        curr = int(file[i][0:vl])
    else:
        curr = int(file[i])
    if ans == 0:
        ans = prev/curr
    else:
        ans = prev / curr * ans
    print(prev, curr)


prev = int(file[-2][file[-2].find("|")+1:])/int(file[-1])
print(ans * 100 * prev)