file = open("input").readlines()

left_list = []
right_list = []
for line in file:
    left_num, right_num = line.strip().split()
    left_list.append(left_num)
    right_list.append(right_num)

left_list = list(map(int, sorted(left_list)))
right_list = list(map(int, sorted(right_list)))
def solve_one():
    total = 0
    for i in range(len(left_list)):
        total += abs(left_list[i] - right_list[i])
    return total
def solve_two():
    total = 0
    for i in left_list:
        count = 0
        for j in right_list:
            if i == j:
                count += 1
        total += count * i
    return total

print(solve_one())
print(solve_two())