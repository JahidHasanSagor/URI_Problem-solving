valueList = [float(x) for x in input().split()]
valueList.sort(reverse=True)
print(valueList)
a = valueList[0]
b = valueList[1]
c = valueList[2]

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
elif a ** 2 == (b ** 2 + c ** 2):
    print("TRIANGULO RETANGULO")
elif a ** 2 > (b ** 2 + c ** 2):
    print("TRIANGULO OBTUSANGULO")
elif a ** 2 < (b ** 2 + c ** 2):
    print("TRIANGULO ACUTANGULO")
if a == b == c:
    print("TRIANGULO EQUILATERO")
elif (a == b and a != c) or (a == c and c != b) or (b == c and b != a):
    print("TRIANGULO ISOSCELES")
