value = float(input())


def calPercentage(value, percentage):
    return (value * percentage) / 100


if value > 2000.00:
    if value > 3000.00:
        if value > 4500.00:
            value1 = value - 3000.00
            value2 = value - 4500.00
            tax = calPercentage((value - 4500.00), 28) + calPercentage(((value - value2) - 3000.00), 18) + calPercentage(((value - value1) - 2000.00), 8)
            print("R$ %.2f" % tax)
        else:
            tax1 = value - 3000.00
            tax = calPercentage((value - 3000.00), 18) + calPercentage(((value - tax1) - 2000.00), 8)
            print("R$ %.2f" % tax)
    else:
        tax = calPercentage((value - 2000.00), 8)
        print("R$ %.2f" % tax)
else:
    print("Isento")
