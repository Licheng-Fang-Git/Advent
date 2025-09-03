from functools import cache

file = open("../input").read().split("\n\n")

@cache
def check_design(towels, designs, original_design, current_design):

    if original_design == current_design:
        return 1
    elif designs == "":
        return 0

    possible_towels = []
    valid = 0

    for towel in towels:
        if designs[0] in towel:
            possible_towels.append(towel.strip())

    for towel in possible_towels:
        towel_length = len(towel)
        towel_place = towel.find(towel)
        if designs[towel_place:towel_length] == towel:
            valid += check_design(towels, designs[towel_length:], original_design, current_design + towel)

        else:
            continue

    return valid

towels_list, designs_list = file
towels_list = tuple(towels_list.split(","))
designs_list = tuple(designs_list.split("\n"))

total = 0
for design in designs_list:
    total += check_design(towels_list, design, design, "")


print(total)

