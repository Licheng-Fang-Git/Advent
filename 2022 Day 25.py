file = open("input").readlines()


def convert_to_decimal(string_coded):
    length = len(string_coded) - 1
    decimal = 0
    for i in range(len(string_coded)):
        convert = string_coded[length - i]
        if convert == "-":
            convert = -1
        elif convert == "=":
            convert = -2
        decimal += 5 ** i * int(convert)
    return decimal


# def convert_to_SNAFU(decimal_num):
#     snafu_number = 0
#     snafu_string = ""
#     while decimal_num > 0:
#         exponent = 0
#         while 5 ** (exponent + 1) <= decimal_num:
#             exponent += 1
#         snafu_number += 5 ** exponent
#         decimal_num -= snafu_number
#     return snafu_number

def recurse_SNAFU(decimal_num, SNAFU_num, SNAFU_string, exponent_index):
    if decimal_num - SNAFU_num == 0:
        return SNAFU_string
    if SNAFU_num > decimal_num:
        return

    possible_paths = [-2, -1, 0, 1, 2]

    for path in possible_paths:
        pass


total = 0
for line in file:
    coded = line.strip()
    print(coded)
    total += convert_to_decimal(coded)

# len(exponenet_index) -- > [0,0,0,0]
