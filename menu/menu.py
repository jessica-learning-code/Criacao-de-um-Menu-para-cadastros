from pathlib import Path

PASTA_DO_PROGRAMA = Path(__file__).parent
ARQUIVO = PASTA_DO_PROGRAMA / 'cadastros.txt'

def leiaTexto(msg):
    while True:
        l = input(msg)
        if l == "":
            print("ERRO, entrada vazia!")
            continue
        if not l.isalpha():
            print("ERRO, digite uma entrada válida!")
            continue
        return str(l)

def leiaInt(msg):
    while True:
        n = str(input(msg)).strip()
        if n == "":#se n receber um valor vazio,mostra-rá erro
            print(f'\033[0;31mERRO, entrada vazia!\033[m')
            continue
        if not n.isdigit():#se n não for apenas digitos de 0-9,dá erro
            print(f'\033[0;31mERRO, digite apenas números!\033[m')
            continue
        return int(n)
    
def ver_cadastros():
    try:
        with open(ARQUIVO,'r',encoding='utf-8') as arquivo:
            print('-'*50)
            print(f'{'LISTA DE CADASTRADOS':^50}')
            print('-'*50)
            print(arquivo.read().strip())
    except FileNotFoundError:
        print('\nNenhum cadastro realizado ainda.')

def cadastrar():
    print('-'*50)
    print(f'{'NOVO CADASTRO':^50}')
    print('-'*50)
    nome = leiaTexto('Digite o nome: ')
    idade = leiaInt('Digite a idade: ')
    with open(ARQUIVO,'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome:<30}{idade:>8} anos\n')
    print(f'\nNovo registro de {nome} adicionado!')

while True:
    print('-'*50)
    print(f'{'MENU PRINCIPAL':^50}')
    print('-'*50)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('-'*50)

    escolher = leiaInt('Escolha uma opção: ')

    if escolher == 1:
        ver_cadastros()
    elif escolher == 2:
        cadastrar()
    elif escolher == 3:
        print('SAINDO...')
        break
    else:
        print('ERRO, digite uma opção válida!')
        continue


