import random
import selenium


def salary_and_kpi():
    salary = int(input('What you salary? '))
    kpi = random.choice([True, False])
    value_kpi = random.random()
    if kpi == True:
        res_salary = int(salary + salary * value_kpi)
        print(f'{salary}, {kpi} - ${res_salary}')
    else:
        print(f'{salary}, {kpi} - ${salary}')


salary_and_kpi()
