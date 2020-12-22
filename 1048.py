salary = float(input())
n_salary = 0
moneyEarned = 0
percentage = 0
if 0 <= salary <= 400.00:
    n_salary = salary + (salary * 0.15)
    moneyEarned = salary * 0.15
    percentage = 15
elif 400.00 < salary <= 800:
    n_salary = salary + (salary * 0.12)
    moneyEarned = salary * 0.12
    percentage = 12
elif 800.00 < salary <= 1200.00:
    n_salary = salary + (salary * 0.10)
    moneyEarned = salary * 0.10
    percentage = 10
elif 1200.00 < salary <= 2000.00:
    n_salary = salary + (salary * 0.07)
    moneyEarned = salary * 0.07
    percentage = 7
elif salary > 2000.00:
    n_salary = salary + (salary * 0.04)
    moneyEarned = salary * 0.04
    percentage = 4
print("Novo salario: %.2f" % n_salary)
print("Reajuste ganho: %.2f" % moneyEarned)
print("Em percentual:", percentage, "%")
