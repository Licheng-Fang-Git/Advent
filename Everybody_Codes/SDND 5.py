file = open('../input').read().split(":")
armor = [[]]
file = list(map(int,file[1].split(",")))

i = 0
while i < len(file):
    if len(armor[0]) == []:
        armor[0].append(file[i])
        continue
