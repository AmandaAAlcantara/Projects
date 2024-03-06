print('-'*20)
print('Plano de Vacinação')
print('-'*20)
vacinaA2 = []
vacinaP2 = []
vacinaC2 = []
vacinaJ2 = []
doses = []
vacinaA = []
vacinaP = []
vacinaC = []
vacinaJ = []

dose = input('Qual dose sera aplicada? primeira <1> ou segunda <2>: ')
while dose != '':
    if dose == '1':
        gestante = input('Pessoa a receber dose e gestante ou puérpera? <S> para sim ou <N> para não: ')
        if gestante == "S":
            vacinaP.append(gestante)
        else:
            comorbidade = input('Possui comorbidade? <S> para sim e <N> para não: ')
            if comorbidade == 'S':
                vacinaP.append(comorbidade)
            else:
                idade = float(input('Idade: '))
                if 18 <= idade <=30:
                    vacinaJ.append(idade)
                elif idade>= 60:
                    vacinaP.append(idade)
                else:
                    vacinaA.append(idade) 
        dose = input('Qual dose sera aplicada <1> ou <2>, para encerrar dados <ENTER>: ')
    else:
        vacina = input('Qual foi a vacina aplicada na primeira dose? AstraZeneca, Pfizer, CoronaVac ou Jansen: ')
        if vacina == 'AstraZeneca':
            vacinaA2.append(vacina)
        elif vacina == 'Pfizer':
            vacinaP2.append(vacina)
        elif vacina == 'CoronaVac':
            vacinaC2.append(vacina)
        else:
            vacinaJ2.append(vacina)
        doses.append(dose)
        dose = input('Qual dose sera aplicada <1> ou <2>, para encerrar dados <ENTER>: ')
        
print('Dados encerrados')


dosesvacinaA = (len(vacinaA)*2) + len(vacinaA2)
dosesvacinaC = (len(vacinaC)*2) + len(vacinaC2)
dosesvacinaP = (len(vacinaP)*2) + len(vacinaP2)
dosesvacinaJ = (len(vacinaJ)*2) + len(vacinaJ2)
print('Doses necessárias de Pfzier:',dosesvacinaP)
print('Doses necessárias de Jansen:',dosesvacinaJ)
print('Doses necessárias de CoronaVac:',dosesvacinaC)
print('Doses necessárias de AstraZeneca:',dosesvacinaA)

input('')