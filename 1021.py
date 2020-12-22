x = float(input())


print("NOTAS:")
note100 = int((x / 100))
notes50 = x % 100
print(note100, "nota(s) de R$ 100.00")

note50 = int(notes50 / 50)
notes20 = notes50 % 50
print(note50, "nota(s) de R$ 50.00")

note20 = int(notes20 / 20)
notes10 = notes20 % 20
print(note20, "nota(s) de R$ 20.00")

note10 = int(notes10 / 10)
notes5 = notes10 % 10
print(note10, "nota(s) de R$ 10.00")

note5 = int(notes5 / 5)
notes2 = notes5 % 5
print(note5, "nota(s) de R$ 5.00")

note2 = int(notes2 / 2)
notes1 = notes2 % 2
print(note2, "nota(s) de R$ 2.00")

print("MOEDAS:")

y = x - int(x)

moeda1 = int(notes1 / 1)
moedas0_50 = notes1 % 1
print(moeda1, "moeda(s) de R$ 1.00")

moeda0_50 = int(moedas0_50 / 0.5)
moedas0_25 = moedas0_50 % 0.5
print(moeda0_50, "moeda(s) de R$ 0.50")

moeda0_25 = int(moedas0_25 / 0.25)
moedas0_10 = moedas0_25 % .25
print(moeda0_25, "moeda(s) de R$ 0.25")

moeda0_10 = int(moedas0_10 / .10)
moedas0_05 = moedas0_10 % .10
print(moeda0_10, "moeda(s) de R$ 0.10")

moeda0_05 = int(moedas0_05 / .05)
moedas0_01 = moedas0_05 % .05
print(moeda0_05, "moeda(s) de R$ 0.05")

moeda0_01 = int(moedas0_01 / .01)
moeda = moedas0_01 % .01
print(moeda0_01, "moeda(s) de R$ 0.01")
