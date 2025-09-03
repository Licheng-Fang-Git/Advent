file = open("/input").read().split("\n")

def solve_one(number):

    number = (number ^ (number * 64)) % 16777216
    number = (number ^ (number // 32)) % 16777216
    number = (number ^ (number * 2048)) % 16777216
    return number
price_patterns = {}
total_one = 0
for line in file:
    secret_num = int(line)
    print(secret_num)
    original_pattern = [secret_num%10]
    for _ in range(10):
        secret_num = solve_one(secret_num)
        pattern_num = secret_num
        while len(original_pattern) <= 4:
            original_pattern.append(pattern_num % 10)
            pattern_num = solve_one(pattern_num)
        o1, o2, o3, o4, o5 = original_pattern
        print(o1, o2, o3, o4, o5)
        n1, n2, n3, n4 = o2 - o1, o3 - o2, o4 - o3, o5 - o4
        print(n1, n2, n3, n4)
        price_patterns[o1, o2, o3, o4] = [n1, n2, n3, n4]
        original_pattern.clear()
    total_one += secret_num

print(price_patterns)

