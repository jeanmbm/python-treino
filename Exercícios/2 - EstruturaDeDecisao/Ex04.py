# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('\nDigite uma letra: ')

if letra.lower() == 'a' or letra.lower() == 'e' or letra.lower() == 'i' or letra.lower() == 'o' or letra.lower() == 'u':
    print('\nÉ uma vogal')
else:
    print('\nÉ uma consoante')
