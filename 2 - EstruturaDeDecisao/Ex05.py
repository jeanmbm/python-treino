# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

letra = input(
    'Qual turno você estuda? \nM - Matutino \nV - Verspetino \nN - Noturno \nR: ')

if letra.upper() == 'M':
    print('\nBom Dia!')
elif letra.upper() == 'V':
    print('\nBoa Tarde!')
elif letra.upper() == 'N':
    print('\nBoa Noite!')
else:
    print('\nValor Inválido')
