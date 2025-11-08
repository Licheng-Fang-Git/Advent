file = open('../input').read()

r = [0,0]
comma = file.find(",")
a = [int(file[3:comma]), int(file[comma+1:len(file)-1])]
print(a[0], a[1])
def multiply(r):
    x1, y1 = r[0], r[1]
    x2, y2 = r[0], r[1]
    r[0] = x1 * x2 - y1 * y2
    r[1] = x1 * y2 + y1 * x2

def divide(r):
    x1, y1 = r[0], r[1]
    x2, y2 = 10, 10
    r[0] = x1 // x2
    r[1] = y1 // y2

def add(r):
    x1, y1 = r[0], r[1]
    x2, y2 = a[0], a[1]
    r[0] = x1 + x2
    r[1] = y1 + y2

for _ in range(3):
    multiply(r)
    divide(r)
    add(r)

print(r)
