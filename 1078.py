number = int(input())
for x in range(1, 11):
    result = "{} x {} = {}"
    print(result.format(x, number, x*number))
