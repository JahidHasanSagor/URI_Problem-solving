import math as m

x1, y1 = [float(x) for x in input("Enter two value: ").split()]
x2, y2 = [float(x) for x in input("Enter two value: ").split()]
distance = m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("%.4f" % distance + "\n")
