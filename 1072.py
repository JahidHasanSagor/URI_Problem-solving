
number = int(input())
if number > 10000:
    number = int(input())

array = []
for x in range(number):
    array.append(int(input()))
inn = 0
out = 0
for y in array:
    if 10 <= y <= 20:
        inn = inn + 1
    else:
        out = out + 1

print(str(inn) + " in")
print(str(out) + " out")
