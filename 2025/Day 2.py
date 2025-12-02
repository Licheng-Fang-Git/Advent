file = open('../input').read().split(',')
def part_one():
    ans = 0
    for id_ranges in file:
        start, end = map(int, id_ranges.split("-"))
        for i in range(start, end+1):
            i = str(i)
            if len(i) % 2 != 0:
                continue
            middle = len(i)//2
            if i[:middle] == i[middle:]:
                ans += int(i)
    return ans

def part_two():
    ans = 0
    for id_ranges in file:
        start, end = map(int, id_ranges.split("-"))
        for i in range(start, end+1):
            i = str(i)
            length_num = len(i)
            for j in range(2, length_num+1):
                if length_num % j != 0:
                    continue
                mid = length_num // j
                seq = i[:mid]
                left = 0
                right = mid
                matches = True
                while matches and right <= len(i):
                    if seq != i[left:right]:
                        matches = False
                    left += mid
                    right += mid
                if matches:
                    print(int(i))
                    ans += int(i)
                    break
    return ans

# print(part_one())
print(part_two())




