# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#   par ou ímpar;
#   positivo ou negativo;
#   inteiro ou decimal.

primeiro_valor = float(input('Digite um valor: '))
segundo_valor = float(input('Digite outro valor: '))

isPassed = False
while (not isPassed):
    operação = input(
        'Informe o símbolo da operação que deseja realizar: \nsoma (+) \nsubtração (-) \nmultiplicação (*) \ndivisão (/) \nR: ')
    if operação == '+':
        resultado = primeiro_valor + segundo_valor
        isPassed = True
    elif operação == '-':
        resultado = primeiro_valor - segundo_valor
        isPassed = True
    elif operação == '*':
        resultado = primeiro_valor * segundo_valor
        isPassed = True
    elif operação == '/':
        resultado = primeiro_valor / segundo_valor
        isPassed = True
    else:
        print('\n!! Símbolo Inválido !!')
