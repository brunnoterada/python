lista = []
list(lista)
dados = dict()
lista18 = []
lista_de_menor = []
dados['nome'] = str(input('Nome: ')).title()
while dados['nome'] != '':
    dados['idade'] = int(input('Idade: '))
    dados['telefone'] = int(input('Telefone: '))
    lista.append(dados.copy())
    dados['nome'] = str(input('Nome: ')).title()
print(f'{"NOME":<15}{"IDADE":<10}{"TELEFONE":<10}')
for contatos in lista:
    print(f'{contatos["nome"]:<15}{contatos["idade"]:<10}{contatos["telefone"]:<10}')
    if contatos['idade'] >= 18:
        lista18.append(contatos.copy())
    if contatos['idade'] < 18:
        lista_de_menor.append(contatos.copy())
print('-='*60)
print('LISTA TELEFÔNICA COM DE MAIOR')
print(f'{"NOME":<15}{"IDADE":<10}{"TELEFONE":<10}')
for contatos1 in lista18:
    print(f'{contatos1["nome"]:<15}{contatos1["idade"]:<10}{contatos1["telefone"]:<10}')
print('-='*60)
print('LISTA TELEFÔNICA COM DE MENOR')
print(f'{"NOME":<15}{"IDADE":<10}{"TELEFONE":<10}')
for contatos1 in lista_de_menor:
    print(f'{contatos1["nome"]:<15}{contatos1["idade"]:<10}{contatos1["telefone"]:<10}')