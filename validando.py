def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mEntrada inválida!\033[m')
            continue
        except KeyboardInterrupt:
            print('O Usuário interrompeu o programa!') 
        else:    
            return n

def leiaFloat(msg):
    while True:
        try:
            m = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mEntrada inválida!\033[m')
            continue
        except KeyboardInterrupt:
            print('O Usuário interrompeu o programa!') 
        else:
            return m
        
        
n = leiaInt('Digite um número inteiro: ')
m = leiaFloat('Digite um número real: ')
print(f'Os números digitados são {n} e {m}')

    