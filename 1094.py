val = int(input())
c = 0
r = 0
s = 0
for total_C in range(val):
    a, b = list(map(str, input().split()))
    a = int(a)
    if b == 'C':
        c += a
    elif b == 'R':
        r += a
    else:
        s += a

total = c + r + s
total_C = (c * 100) / total
total_R = (r * 100) / total
total_S = (s * 100) / total

print("Total: {} cobaias".format(total))
print("Total de coelhos:", c)
print("Total de ratos:", r)
print("Total de sapos:", s)
print("Percentual de coelhos: %.2lf %%" % total_C)
print("Percentual de ratos: %.2lf %%" % total_R)
print("Percentual de sapos: %.2lf %%" % total_S)
