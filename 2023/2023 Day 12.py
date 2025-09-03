from functools import cache


file = open("../input").readlines()

nums = tuple((1,2,3))

# ???.### 1,1,3
@cache
def check_garden(garden, sequences_list, hash_streak ):
    if garden == "":
        if len(sequences_list) == 0 and hash_streak == 0:
            return 1
        else:
            return 0

    valid = 0
    if garden[0] == "?":
        possible_symbols = [".", "#"]
    else:
        possible_symbols = garden[0]

    for symbols in possible_symbols:
        if symbols == "#":
            valid += check_garden(garden[1:], sequences_list, hash_streak + 1)
        else:
            if hash_streak != 0:
                comma = sequences_list.find(",")
                if comma != -1:
                    if len(sequences_list) != 0 and hash_streak == int(sequences_list[:comma]):
                        valid += check_garden(garden[1:], sequences_list[comma+1:], 0)
                else:
                    if len(sequences_list) != 0 and hash_streak == int(sequences_list):
                        valid += check_garden(garden[1:], sequences_list[20:], 0)
            else:
                valid += check_garden(garden[1:], sequences_list, 0)

    return valid

total = 0

for line in file:
    garden_line = line.split()[0]
    pattern = line.split()[1]
    new_pattern =  pattern
    for _ in range(4):
        new_pattern += "," + pattern
    print("?".join([garden_line] * EXPAND) + ".", new_pattern)
    total += check_garden(garden_line, new_pattern, 0 )

print(total)