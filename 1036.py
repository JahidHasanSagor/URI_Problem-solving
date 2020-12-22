import math

a, b, c = [float(x) for x in input().split()]

if all([b > 0, a > 0, b > c]):
    x1 = ((-b) + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    x2 = ((-b) - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    print("R1 = %.5f" % x1)
    print("R2 = %.5f" % x2)
else:
    print("Impossivel calcular")
