number = int(input())
array = []
for x in range(number):
    array.append(int(input()))

for y in array:
    if y > 0 and y % 2 == 0:
        print("EVEN POSITIVE")
    elif y < 0 and y % 2 == 0:
        print("EVEN NEGATIVE")
    elif y < 0 and y % 2 != 0:
        print("ODD NEGATIVE")
    elif y > 0 and y % 2 != 0:
        print("ODD POSITIVE")
    else:
        print("NULL")
