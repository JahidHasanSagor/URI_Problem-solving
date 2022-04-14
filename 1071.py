x = int(input())
y = int(input())
z = range(y + 1, x)
sum = 0
for i in z:
    if i % 2 != 0:
        sum += i

print(sum)
