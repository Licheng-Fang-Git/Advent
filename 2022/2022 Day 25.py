file = open("../input").readlines()


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

def convert_to_snafu(decimal_num):
    snafu = ""
    while decimal_num:
        rem = decimal_num % 5
        decimal_num //= 5
        print(snafu, rem)
        if rem <= 2:
            snafu = str(rem) + snafu
        else:
            rem = "   =-"[rem]
            snafu = rem + snafu
            decimal_num += 1

    return snafu

total = 0
for line in file:
    coded = line.strip()
    total += convert_to_decimal(coded)

print(convert_to_snafu(3))
