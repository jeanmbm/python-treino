# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   a. o produto do dobro do primeiro com metade do segundo .
#   b. a soma do triplo do primeiro com o terceiro.
#   c. o terceiro elevado ao cubo.

primeiroNumero = input('Digite um valor inteiro: ')
segundoNumero = input('Digite outro valor inteiro: ')
valorReal = input('Digite um valor com casas decimais (real): ')

a = (2 * int(primeiroNumero)) * (int(segundoNumero) / 2)
b = 3 * int(primeiroNumero) + 3 * float(valorReal)
c = float(valorReal)**2

print('\nPrimeiro valor: ', primeiroNumero, '\nSegundo valor: ',
      segundoNumero, '\nTerceiro valor: ', valorReal)
print('Produto do dobro do primeiro valor com metade do segundo valor: ', a)
print('Soma do triplo do primeiro valor com o terceiro valor: ', b)
print('Terceiro valor elevado ao cubo: ', c)
