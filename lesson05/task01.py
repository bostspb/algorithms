"""
Задача №1
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

Company = namedtuple('Company', ['name', 'profit', 'average_profit'])

companies_number = int(input('Enter the number of companies:\n'))
companies = list()
all_companies_profit = list()

for i in range(1, companies_number + 1):
    company_name = input(f'Enter the company name #{i}:\n')
    company_profit = []
    for quarter in range(1, 5):
        profit = int(input(f'Enter the company\'s profit for the {quarter} quarter:\n'))
        company_profit.append(profit)
        all_companies_profit.append(profit)
    average_profit = sum(company_profit) / 4
    company = Company(company_name, company_profit, average_profit)
    companies.append(company)

print(f'Companies list:\n{companies}')
average_profit = sum(all_companies_profit) / len(all_companies_profit)
print(f'Average profit: {average_profit}')

leaders = list()
losers = list()
for company in companies:
    if company.average_profit >= average_profit:
        leaders.append(company)
    else:
        losers.append(company)

print(f'Companies whose profit is above average:\n{leaders}\n')
print(f'Companies whose profit is below average:\n{losers}')
