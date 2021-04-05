validador = input('Deseja saber sua categoria de lutador?(sim/não) ')


while(validador !=  'não'):

    print('**************************************')
    nomelutador = input('Qual o nome do Lutador? ')
    print('**************************************')
    pesolutador = float(input('Qual o peso do Lutador? '))
    print('**************************************')

    if pesolutador < 65 :
        categorialutador = 'Pena'

    elif pesolutador >= 65 and pesolutador < 72:
        categorialutador = 'Leve'

    elif pesolutador >= 72 and pesolutador < 79:
        categorialutador = 'Ligeiro'

    elif pesolutador >= 79 and pesolutador < 86:
        categorialutador = 'Meio-médio'

    elif pesolutador >= 86 and pesolutador < 93:
        categorialutador = 'Médio'

    elif pesolutador >= 93 and pesolutador < 100:
        categorialutador = 'Meio-pesado'

    else:
        categorialutador = 'Pesado'

    print('Nome fornecido: {}.'.format(nomelutador))
    print('')
    print('Peso fornecido: {}.'.format(pesolutador))
    print('')
    print('O lutador {} pesa {} kg e se enquadra na categoria {}'.format(nomelutador,pesolutador,categorialutador))
    print('**************************************')
    validador = input('Deseja saber sua categoria de lutador?(sim/não) ')
print('Encerrando o programa')