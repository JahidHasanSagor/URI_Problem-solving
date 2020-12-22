a, b, c, d = [float(x) for x in input("Enter two value: ").split()]

if all([b > c, d > a, (c + d) > (a + b), c > 0, d > 0, a % 2 == 0]):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
