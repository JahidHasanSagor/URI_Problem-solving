start, end = [int(x) for x in input().split()]

hour = end - start

if hour < 0:
    hour = 24 + (end - start)
    print("O JOGO DUROU", hour, "HORA(S)")
elif end == start:
    print("O JOGO DUROU 24 HORA(S)")
else:
    print("O JOGO DUROU", hour, " HORA(S)")
