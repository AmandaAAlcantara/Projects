print('-'*21)
print('Exercício recrutamento pessoal ACME')
print('-'*21)

ListaNome = []
ListaSexo = []
ListaSalario =[]
nome = (input('Digite nome <ou ENTER> para encerrar: '))
if (nome == '') or (nome == ' '):
    print('Dados não informados')
else:   
    while nome != '':
        sexo = input('Digite sexo, <F> para Feminino ou <M> Masculino: ')
        while (sexo != 'F') and (sexo != 'M'):
            print('Erro, informação inválida')
            sexo = input('Digite sexo, <F> para Feminino ou <M> Masculino: ')
        salario = float(input('Forneça o valor do salário: R$'))
        while (salario < 0):
            print('Erro, informação inválida')
            salario = float(input('Forneça o valor do salário: R$'))
        ListaNome.append(nome)
        ListaSexo.append(sexo)
        ListaSalario.append(salario)
        nome = input('Digite um novo nome <ou ENTER> para encerrar: ')
    
    print('-'*20)
    print('Lista completa dos candidatos')
    print('NOME         SEXO      SALÁRIO')
    n = 0
    while n< len(ListaNome):
        print(ListaNome[n],'       ',ListaSexo[n],'        ',ListaSalario[n])
        n = n + 1

    print('-'*20)
    print('RESPOSTAS: ')
    
    
    maiorsalario = max(ListaSalario)
    i = ListaSalario.index(maiorsalario)
    print('Nome da pessoa com o maior salário: {}'.format(ListaNome[i]))

    if 'F' in ListaSexo:
        ListaF = []
        ListaNF = []
        f = 0
        while f< len(ListaSexo):
            if 'F' in ListaSexo[f]:
                ListaF.append(ListaSalario[f])
                ListaNF.append(ListaNome[f])
                maiorsalario2 = max(ListaF)
                msf = ListaF.index(maiorsalario2)
            f = f + 1
        print('Nome da pessoa do sexo feminino com maior salário é: {}'.format(ListaNF[msf])) 
    else:
        print('Nome da pessoa do sexo feminino com maior salário é: Candidatas não foram cadastradas!')

    if 'M' in ListaSexo:
        ListaM = []
        s = 0
        while s< len(ListaSexo):
            if 'M' in ListaSexo[s]:
                ListaM.append(ListaSalario[s])   
            s = s + 1
        z = 0
        total = 0
        while z< len(ListaM):
            total = total + ListaM[z]
            z = z + 1
        msm = total/z
        print('Valor do salário médio dentre as pessoas do sexo masculino: R${}'.format(msm)) 
    else:
        print('Valor do salário médio dentre as pessoas do sexo masculino: Candidatos não foram cadastrados!') 
        




    





    
