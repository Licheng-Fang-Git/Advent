file = open("input").readlines()

def solve(target, array, current, idx):

    if target == current and idx + 1 == len(array):
        return target

    if idx + 1 == len(array):
        return 0

    if current + array[idx + 1] <= target:
        total = solve(target, array, current + array[idx+ 1], idx + 1)
        if total == target:
            return target

    if current * array[idx + 1] <= target:
        total = solve(target, array, current * array[idx+ 1], idx + 1)
        if total == target:
            return target

    # if int(str(current) +  str(array[idx + 1])) <= target:
    #     total = solve(target, array, int(str(current) + str(array[idx+ 1])), idx + 1)
    #     if total == target:
    #         return target

    return 0

target_sum = 0
for line in file:
    target, numbers = line.split(":")
    array_num = list(map(int, numbers.split()))
    target = int(target)
    target_sum += solve(target, array_num, array_num[0], 0)

print(target_sum)

