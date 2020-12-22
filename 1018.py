x = int(input())

note100 = (x // 100)
notes50 = x % 100
print(note100, "nota(s) de R$ 100,00")

note50 = notes50 // 50
notes20 = notes50 % 50
print(note50, "nota(s) de R$ 50,00")

note20 = notes20 // 20
notes10 = notes20 % 20
print(note20, "nota(s) de R$ 20,00")

note10 = notes10 // 10
notes5 = notes10 % 10
print(note10, "nota(s) de R$ 10,00")

note5 = notes5 // 5
notes2 = notes5 % 5
print(note5, "nota(s) de R$ 5,00")

note2 = notes2 // 2
notes1 = notes2 % 2
print(note2, "nota(s) de R$ 2,00")

note1 = notes1 // 1
note = notes1 % 1
print(note1, "nota(s) de R$ 1,00")
