x = int(input())

year = x // 365
months = x % 365

month = months // 30
days = months % 30

print(year, "ano(s)")
print(month, "mes(es)")
print(days, "dia(s)")
