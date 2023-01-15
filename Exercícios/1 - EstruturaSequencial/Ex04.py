# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

primeiraNota = input('Digite a primeira nota: ')
segundaNota = input('Digite a segunda nota: ')
terceiraNota = input('Digite a terceira nota: ')
quartaNota = input('Digite a quarta nota: ')

media = (int(primeiraNota) + int(segundaNota) +
         int(terceiraNota) + int(quartaNota)) / 4

print('Sua média é ', media)
