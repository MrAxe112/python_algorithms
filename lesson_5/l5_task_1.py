"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего. """

import collections

QUARTERS = 4
total_profit = 0
companies_list = []

Company = collections.namedtuple('Company', ['name', 'quarters', 'profit'])
number_of_companies = int(input("Введите количество предприятий: "))

for a in range(number_of_companies):
    profit = 0
    quarters = []
    name = str(input(f'Введите название предприятия {a + 1}: '))

    for b in range(QUARTERS):
        quarters.append(float(input(f'Прибыль за {b + 1}-й квартал: ')))
        profit += quarters[b]

    company = Company(name=name, quarters=tuple(quarters), profit=profit)
    companies_list.append(company)
    total_profit += profit

average_profit = total_profit / number_of_companies

print('*' * 120)
print(f'Средняя прибыль = {average_profit:.2f}')

if number_of_companies == 1:
    print(f"ПОлученны данные для 1го предприятия: {companies_list[0].name}. "
          f"Eго годовая прибыль: {companies_list[0].profit:.2f}")
else:
    print(f'Предприятия в списке, прибыль которых выше среднего:')
    for company in companies_list:
        if company.profit > average_profit:
            print(f'Компания {company.name} заработала {company.profit:.2f}')
    print(f'Предприятия в списке, прибыль которых ниже среднего:')
    for company in companies_list:
        if company.profit < average_profit:
            print(f'Компания {company.name} заработала {company.profit:.2f}')
