def part_one(num):
    #steps:
    num = (num ^ (num *64)) % 16777216
    num = (num ^ (num // 32)) % 16777216
    num =  (num ^ (num * 2048)) % 16777216
    return num

total = 0
seqs_total = {}
for lines in open("input"):
    line = int(lines)
    buyer = [line % 10]
    for _ in range(2000):
        line = part_one(line)
        buyer.append(line%10)
    seen = set()
    for i in range(len(buyer) - 4):
        a, b, c, d, e =  buyer[i:i+5]
        seq = (b-a, c-b, d-c, e-d)
        if seq in seen: continue
        seen.add(seq)
        if seq not in seqs_total:
            seqs_total[seq] = 0
        seqs_total[seq] += e

max_banana =  max(seqs_total.values())
print(max_banana)


