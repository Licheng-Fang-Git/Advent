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
def part_two():
    total = 0
    for bank in file:
        length = 12
        battery = ""
        prev_pos = 0
        while length >= 1:
            max_battery = 0
            if battery == "":
                start = 0
            else:
                start = prev_pos + 1
                print(start, len(bank), )
            for i in range(start, len(bank)):
                if len(bank) - i < length:
                    continue
                if int(bank[i]) > max_battery and len(bank) - i >= length:
                    print(i,bank[i], max_battery, len(bank) - i, length)
                    max_battery = int(bank[i])
                    prev_pos = i

            battery += str(max_battery)
            length -= 1
            print(battery)
        total += int(battery)

    print(total)


# print(part_one())
part_two()


