x = int(input())

hr = x // 3600
hr2 = x % 3600

m = hr2 // 60
m2 = hr2 % 60
print(hr, m, m2, sep=':')
