# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input('Digite seu sexo - F (feminino) ou M (masculino): ')

if letra.upper() == 'F':
    print('F - Feminino')
elif letra.upper() == 'M':
    print('M - Masculino')
else:
    print('Sexo Inválido')
