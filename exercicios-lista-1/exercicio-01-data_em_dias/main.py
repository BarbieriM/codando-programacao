# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa
# pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.


from datetime import datetime


date_of_birth = datetime.strptime(input('Informe sua data de nascimento (DD/MM/AAAA) -> '), '%m/%d/%Y')

date_now = datetime.now()

n_years = date_now.year -  date_of_birth.year 
n_months = date_now.month -  date_of_birth.month 
n_days = date_now.day -  date_of_birth.day 

total_days = n_days + (n_months * 30) + (n_years * 365)

print(f'Sua idade em dias é: {total_days}')