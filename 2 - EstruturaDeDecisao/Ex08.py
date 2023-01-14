# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#     Média de Aproveitamento  Conceito
#     Entre 9.0 e 10.0        A
#     Entre 7.5 e 9.0         B
#     Entre 6.0 e 7.5         C
#     Entre 4.0 e 6.0         D
#     Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

primeira_nota = float(input('\nDigite a primeira nota do aluno: '))
segunda_nota = float(input('Digite a segunda nota do aluno: '))

media = (primeira_nota + segunda_nota) / 2

print('\n1° Nota: {} \n2° Nota: {} \nMédia: {}'.format(
    primeira_nota, segunda_nota, media))

if media >= 9:
    print('Conceito: A \nAPROVADO!!')
elif media >= 7.5:
    print('Conceito: B \nAPROVADO!!')
elif media >= 6:
    print('Conceito: C \nAPROVADO!!')
elif media >= 4:
    print('Conceito: D \nREPROVADO')
else:
    print('Conceito: E \nREPROVADO')
