block1, block2 = open("../input").read().split('\n\n')
def part_one():
    count = 0
    for ingredient in list(map(int, block2.split("\n"))):
        for ingredient_ranges in block1.split("\n"):
            start, end = map(int, ingredient_ranges.split("-"))
            if start <= ingredient <= end:
                count += 1
                break
    return count

def part_two():
    count = 0
    all_ranges = sorted([ (int(ingredient_ranges.split("-")[0]), int(ingredient_ranges.split("-")[1])) for ingredient_ranges in block1.split("\n")])
    last_range = None
    for ingredient_range in all_ranges:
        low, high = ingredient_range
        if last_range is None:
            last_range = ingredient_range
        elif last_range[1] < low:
            count += last_range[1] - last_range[0] + 1
            last_range = (low, high)
        else:
            last_range = (last_range[0], max(last_range[1], high))
    count += last_range[1] - last_range[0] + 1
    return count

print(part_two())

