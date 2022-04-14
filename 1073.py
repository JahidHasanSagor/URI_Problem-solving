number = int(input())
if 5 < number < 2000:
    for x in range(number + 1):
        if x > 0 and x % 2 == 0:
            square = "{}^2 = {}"
            print(square.format(x, x * x))

else:
    number = int(input())
