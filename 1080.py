max_val = 0
location = 0
for x in range(100):
    number = int(input())
    if number > max_val:
        max_val = number
        location = x
print(max_val)
print(location+1)
