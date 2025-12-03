file = open("../input").read().split("\n")


def part_one():
    total = 0
    max_num = 0
    for bank in file:
        print(bank)
        max_num = 0
        for i in range(len(bank)):
            for j in range(i+1, len(bank)):
                max_num = max(int(bank[i]+bank[j]),max_num)

        total += max_num
    return total

print(part_one())


