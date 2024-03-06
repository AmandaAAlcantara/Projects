# Procedimento para imprimir o menu de opções 


def imprime_menu_principal():
    print('\n'*50)
    print('**************************************')
    print('* <1> 1 - 4 + 9 - 16 + 25 - 36 + ...                        *')
    print('* <2> 1! - 2! + 3! - 4! + ...                                     *')
    print('* <3> 0! + 1! + 1! + 2! + 3! + 5! + ... fibonacci   *')
    print('* <0> Encerrar o programa                                 *')
    print('**************************************') 


def soma_serie01 (n):
    i = 1
    while i <= n:
        (i**2)
        i = i + 1
        return (i)
def soma_serie02 (n):
    fat = 1
    i = 1 
    while i <= n:
        fat = fat*i
        i = i + 1
    return (fat)
def soma_serie03 (n):
    fat = 1
    i = 1 
    while i <= n:
        fat = fat*i
        i = i + 1
    return (fat)


def imp_serie01 (n):
    i = 1
    while i <= n:
        (i**2)
        i = i + 1
        print(i,'+')
        return (i)
def imp_serie02 (n):
    fat = 1
    i = 1 
    while i <= n:
        fat = fat*i
        i = i + 1
        print(i,'!')
    return (fat)
def imp_serie03 (n):
    fat = 1
    i = 1 
    while i <= n:
        fat = fat*i
        i = i + 1
        print(i,"!")
    return (fat)

# Programa Principal

while True:
    imprime_menu_principal()
    op = int(input('Informe o numero da serie escolhida: '))
    while op < 0 or op > 3:
        print('Opcao invalida!!')
        op = int(input('Informe o numero da serie escolhida: '))
    if op == 0:
        print('Encerrando o programa.......')
        break
    else:
        n = int(input('Quantidade de termos da serie escolhida: '))    
        while n <= 0:
            print('Quantidade invalida!!')
            n = int(input('Quantidade de termos da serie escolhida: '))  
    if op == 1:
        print(f'Serie: {imp_serie01(n):} \nSomatorio: {soma_serie01(n)}')
    elif op == 2:
        print(f'Serie: {imp_serie02(n):} \nSomatorio: {soma_serie02(n)}')
    else:
        print(f'Serie: {imp_serie03(n):} \nSomatorio: {soma_serie03(n)}')
    input('Tecle <ENTER>')