# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

grausFahrenheit = input('Digite a temperatura em Fahrenheit: ')

grausCelsius = 5 * ((float(grausFahrenheit) - 32) / 9)

print('\n-------------- Conversor Fahrenheit -> Celsius --------------')
print('Graus Fahrenheit: ', grausFahrenheit,
      '°F \nGraus Celsius: ', grausCelsius, '°C')
