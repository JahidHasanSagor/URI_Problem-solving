a, b, c = [float(x) for x in input().split()]

if (b + c) > a and (b + a) > c and (a + c) > b:
    print("Perimetro = %.1f" % (a + b + c))
else:
    print("Area = %.1f" % (((a + b) / 2) * c))
