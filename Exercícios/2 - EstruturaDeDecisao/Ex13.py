# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#   - Álcool:
#     - até 20 litros, desconto de 3% por litro
#     - acima de 20 litros, desconto de 5% por litro
#   - Gasolina:
#     - até 20 litros, desconto de 4% por litro
#     - acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

quantidade_litros = float(input('Informe a quantidade de litros vendidos: '))
tipo_conbustivel = input(
    'Informe o tipo de combustível: \nA - Álcool \nG - Gasolina \nR: ')
litro_gasolina = 2.5
litro_alcool = 1.9

if tipo_conbustivel.upper() == "A":
    print('\nTipo de combustível: Álcool \nValor do litro R${:.2f}'.format(
        litro_alcool))
    if quantidade_litros <= 20:
        print('Desconto por litro: 3%')
        valor_venda = (litro_alcool - (litro_alcool * 0.03)) * \
            quantidade_litros
    else:
        print('Desconto por litro: 5%')
        valor_venda = (litro_alcool - (litro_alcool * 0.05)) * \
            quantidade_litros
else:
    print('\nTipo de combustível: Gasolina \nValor do litro R${:.2f}'.format(
        litro_gasolina))
    if quantidade_litros <= 20:
        print('Desconto por litro: 4%')
        valor_venda = (litro_gasolina - (litro_gasolina * 0.04)) * \
            quantidade_litros
    else:
        print('Desconto por litro: 6%')
        valor_venda = (litro_gasolina - (litro_gasolina * 0.06)) * \
            quantidade_litros

print('Valor final a ser pago R${:.2f}'.format(valor_venda))
