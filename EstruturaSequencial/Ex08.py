# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorPorHora = input('Quanto você ganha por hora? R: ')
horasTrabalhadas = input('Quantas horas trabalhou no mês? R: ')

salario = float(valorPorHora) * float(horasTrabalhadas)

print('Salário do mês: R$', salario)
