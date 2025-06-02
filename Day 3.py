import re
file = open("input").read().strip()

find_do = r'(do\(\))'
find_dont =  r"(don't\(\))"
find_mul = r'mul(\(\d+,\d+\))'
find_mul_part_one = re.findall(find_mul, file)
find_mul_part_two = re.findall(f"{find_mul}|{find_dont}|{find_do}", file)

def solve_one(mul_string):
    left_parenthesis = mul_string.find("(")
    right_parenthesis = mul_string.find(")")
    comma = mul_string.find(",")
    return int(mul_string[left_parenthesis+1: comma]) * int(mul_string[comma+1: right_parenthesis])

total_one = 0

for i in find_mul_part_one:
    total_one += solve_one(i)

print(total_one)

total_two = 0
# clear all space
start_do = False
for idx, pattern in enumerate(find_mul_part_two):
    if "do()" in pattern:
        start_do = False
        continue
    if "don't()" in pattern:
        start_do = True
        continue
    if start_do is False:
        for value in find_mul_part_two[idx]:
            if value != "":
                total_two += solve_one(value)

print(total_two)
