notasdic = {'nome':[], 'n1':[], 'n2':[], 'n3':[], 'n4':[], 'resultado':[]}

while True:
    cadastronota = input('Deseja cadastrar uma nota? [S/N]')
    if cadastronota.upper() in 'N':
        break

    nome = input('Qual seu nome?')
    n1 = float(input('Qual a primeira nota?'))
    n2 = float(input('Qual a segunda nota?'))
    n3 = float(input('Qual a terceira nota?'))
    n4 = float(input('Qual a quarta nota?'))
    notasdic['nome'].append(nome)
    notasdic['n1'].append(n1)
    notasdic['n2'].append(n2)
    notasdic['n3'].append(n3)
    notasdic['n4'].append(n4)

    media = ((n1 + n2 + n3 + n4) / 4)

    print(media)
    if media > 7:
        resultado = 'aprovado'
    else:
        resultado = 'reprovado'
    notasdic['resultado'].append(resultado)
for i in notasdic.items():
    print(i['nome'])