file = open("../input").read()

a_sum = [0] * (len(file)+1)
b_sum = [0] * (len(file)+1)
c_sum = [0] * (len(file)+1)

ans_a = 0
ans_b = 0
ans_c = 0
for i in range(len(file)-1, -1, -1):
    a_sum[i] = a_sum[i+1]
    b_sum[i] = b_sum[i + 1]
    c_sum[i] = c_sum[i + 1]
    if file[i] == 'a':
        a_sum[i] += 1
    elif file[i] == 'b':
        b_sum[i] += 1
    elif file[i] == 'c':
        c_sum[i] += 1
    if file[i] == "A":
        ans_a += a_sum[i]
    elif file[i] == "B":
        ans_b += b_sum[i]
    elif file[i] == "C":
        ans_c += c_sum[i]


print(ans_a+ans_b+ans_c)
