a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

pcount = 0

number = [a, b, c, d, e, f]
for i in number:
    if i > 0:
        pcount = pcount + 1

print(pcount, "valores positivos")
