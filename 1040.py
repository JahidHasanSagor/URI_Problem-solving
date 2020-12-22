v1, v2, v3, v4 = [float(x) for x in input().split()]


def cal2(x, y):
    avg = (x + y) / 2
    print("Nota do exame: %.1f" % y)
    if avg >= 5.0:
        print("Aluno aprovado.")
    elif avg <= 4.9:
        print("Aluno reprovado.")

    print("Media final: %.1f" % avg)


def result_calc(v11, v22, v33, v44):
    media = ((v11 * 2) + (v22 * 3) + (v33 * 4) + (v44 * 1)) / 10
    print("Media: %.1f" % media)
    if media >= 7.0:
        print("Aluno aprovado.")
    elif media < 5.0:
        print("Aluno reprovado.")
    elif 5.0 <= media <= 6.9:
        print("Aluno em exame.")

        cal2(media, float(input()))
    else:
        print("ok")


result_calc(v1, v2, v3, v4)
