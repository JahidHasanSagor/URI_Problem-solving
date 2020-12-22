startHour, startMin, endHour, endMin = [int(x) for x in input().split()]

hour = endHour - startHour
minutes = endMin - startMin

if hour < 0:
    hour = 24 + (endHour - startHour)
if minutes < 0:
    minutes = 60 + (endMin - startMin)
    hour = hour - 1
if startHour == endHour and endMin == startMin:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU", hour, "HORA(S) E", minutes, "MINUTO(S)")
