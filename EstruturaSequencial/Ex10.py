# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

grausCelsius = input('Digite a temperatura em Celsius: ')

grausFahrenheit = float(grausCelsius) * 1.8 + 32

print('\n-------------- Conversor Celsius -> Fahrenheit --------------')
print('Graus Celsius: ', grausCelsius,
      '°C \nGraus Fahrenheit: ', grausFahrenheit, '°F\n')
