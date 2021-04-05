#função para validar se o número está entre 10000 e 30000
def validanumero(pergunta, min, max):
    numero= int(input(pergunta))
    while((numero < min) or (numero > max)):
        print('_______________________________')
        print('Você digitou um número invalido')
        print('_______________________________')
        numero = int(input(pergunta))
    return numero

def criacodigo(codigo):

    separanumero = str(codigo)

    nun1 = int(separanumero[0]) * 2
    nun2 = int(separanumero[1]) * 3
    nun3 = int(separanumero[2]) * 4
    nun4 = int(separanumero[3]) * 5
    nun5 = int(separanumero[4]) * 6

    soma = nun1 + nun2 + nun3 + nun4 + nun5

    resulatadofinal = soma % 7

    print('Seu código é {}-{}'.format(numero, resulatadofinal))



numero = validanumero('Digite um número entrei 10000 e 30000:',10000,30000)

print('Número digitado foi {}\n'.format(numero))

criacodigo(numero)


