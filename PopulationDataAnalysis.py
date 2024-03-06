dados = [['Argentina',           44270440,  45.4,  34.26,  8.59,  2.64,  8.4,  0.44,  0.21,  0.06],
         ['Armênia',             2931568,   29.0,  46.3,   12.0,  5.6,   2.0,  3.7,   1.0,   0.4],
         ['Austrália',           24642693,  40.0,  31.0,   8.0,   2.0,   9.0,  7.0,   2.0,   1.0],
         ['Áustria',             8592470,   30.0,  33.0,   12.0,  6.0,   7.0,  8.0,   3.0,   1.0],
         ['Barém',               1418695,   48.48, 19.35,  22.61, 3.67,  3.27, 1.33,  1.04,  0.25],
         ['Bangladesh',          164833667, 31.18, 21.44,  34.58, 8.85,  1.39, 0.96,  0.96,  0.64],
         ['Bélgica',             11444053,  38.0,  34.0,   8.6,   4.1,   7.0,  6.0,   1.5,   0.8],
         ['Bolívia',             11053376,  51.53, 29.45,  10.11, 1.15,  4.39, 2.73,  0.54,  0.1],
         ['Bósnia e Herzegovina',3792730,   31.0,  36.0,   12.0,  6.0,   5.0,  7.0,   2.0,   1.0],
         ['Brasil',              211248418, 36.0,  34.0,   8.0,   2.5,   9.0,  8.0,   2.0,   0.5],
         ['Bulgária',            7045097,   28.0,  37.0,   13.0,  7.0,   5.0,  7.0,   2.0,   1.0],
         ['Camboja',             16077172,  46.7,  27.2,   18.5,  4.9,   1.3,  0.8,   0.5,   0.1],
         ['Camarões',            24515533,  42.8,  38.8,   12.0,  3.3,   1.4,  1.2,   0.4,   0.1],
         ['Canadá',              36627140,  39.0,  36.0,   7.6,   2.5,   7.0,  6.0,   1.4,   0.5],
         ['Chile',               18314060,  85.5,  8.7,    3.35,  1.0,   1.2,  0.1,   0.05,  0.1],
         ['China',               1388251023,47.7,  27.8,   18.9,  5.0,   0.28, 0.19,  0.1,   0.03],
         ['Colômbia',            49069267,  61.3,  26.11,  2.28,  1.47,  5.13, 2.7,   0.7,   0.31],
         ['Costa do Marfim',     23869656,  46.5,  22.5,   22.5,  4.3,   2.0,  1.0,   1.0,   0.2],
         ['Croácia',             4207355,   29.0,  36.0,   15.0,  5.0,   5.0,  6.0,   3.0,   1.0],
         ['Cuba',                11486750,  45.8,  33.5,   10.2,  2.9,   3.6,  2.8,   1.0,   0.2],
         ['Chipre',              1189395,   35.22, 40.35,  11.11, 4.72,  3.85, 3.48,  0.87,  0.40]]


#exercicio 1 -----------------------------------------------------------------------------------------
listanomes = []
listaporcentagemTO1 = []
listaporcentagemTA1 = []
listaporcentagemTB1 = []
listaporcentagemAB1 = []
listaporcentagemTO2 = []
listaporcentagemTA2 = []
listaporcentagemTB2 = []
listaporcentagemAB2 = []

for i in range(len(dados)):
    listanomes.append(dados[i][0])

for i in range (len(dados)):
    listaporcentagemTO1.append(dados[i][2])
maior_valora = 0
for i in listaporcentagemTO1:
    if i > maior_valora:
        maior_valora = i
a = listaporcentagemTO1.index(maior_valora)


for i in range (len(dados)):
    listaporcentagemTA1.append(dados[i][3])
maior_valorb = 0
for i in listaporcentagemTA1:
    if i > maior_valorb:
        maior_valorb = i
b = listaporcentagemTA1.index(maior_valorb)


for i in range (len(dados)):
    listaporcentagemTB1.append(dados[i][4])
maior_valorc = 0
for i in listaporcentagemTB1:
    if i > maior_valorc:
        maior_valorc = i
c = listaporcentagemTB1.index(maior_valorc)

for i in range (len(dados)):
    listaporcentagemAB1.append(dados[i][5])
maior_valord = 0
for i in listaporcentagemAB1:
    if i > maior_valord:
        maior_valord = i
d = listaporcentagemAB1.index(maior_valord)

for i in range (len(dados)):
    listaporcentagemTO2.append(dados[i][6])
maior_valore = 0
for i in listaporcentagemTO2:
    if i > maior_valore:
        maior_valore = i
e = listaporcentagemTO2.index(maior_valore)

for i in range (len(dados)):
    listaporcentagemTA2.append(dados[i][7])
maior_valorf = 0
for i in listaporcentagemTA2:
    if i > maior_valorf:
        maior_valorf = i
f = listaporcentagemTA2.index(maior_valorf)

for i in range (len(dados)):
    listaporcentagemTB2.append(dados[i][8])
maior_valorg = 0
for i in listaporcentagemTB2:
    if i > maior_valorg:
        maior_valorg = i
g = listaporcentagemTB2.index(maior_valorg)

for i in range (len(dados)):
    listaporcentagemAB2.append(dados[i][9])
maior_valorh = 0
for i in listaporcentagemAB2:
    if i > maior_valorh:
        maior_valorh = i
h = listaporcentagemAB2.index(maior_valorh)
print('EXERCÍCIO 1: ')
print('_'*60)
print('País       TO+   TA+   TB+   AB+   TO-   TA-   TB-   AB-')
print(listanomes[a],'    ',maior_valora)
print(listanomes[b],'        ',maior_valorb)
print(listanomes[c],'          ',maior_valorc)
print(listanomes[d],'                ',maior_valord)
print(listanomes[e],'                       ',maior_valore)
print(listanomes[f],'                               ',maior_valorf)
print(listanomes[g],'                                      ',maior_valorg)
print(listanomes[h],'                                           ',maior_valorh)               
print('_'*60)

#exercicio 2 ------------------------------------------------------------------------------------------------
print('EXERCÍCIO 2:')
j = 0 
while j < len(dados):
    i = 1
    soma = 0
    while i < (len(dados[0]) - 2):
        soma += dados[j][i]
        #print(turma[j][i])
        i += 1
    print('media = {}'.format(soma/21))
    j +=1

print("_"*60)
print('Grupo de países      TO+    TA+    TB+    AB+    TO-    TA-    TB-    AB-')
print('A',       )
print('B',        )
print('C',        )
print("_"*60)

#exercicio 3 ------------------------------------------------------------------------------------------------
dicionário  = {'Argentina':44270440,
'Armênia':2931568,
'Austrália':24642693,
'Áustria':8592470,
'Barém':1418695,
'Bangladesh':164833667,
'Bélgica':11444053,
'Bolívia':11053376,
'Bósnia e Herzegovina':3792730,
'Brasil':211248418,
'Bulgária':7045097,
'Camboja':16077172,
'Camarões':24515533,
'Canadá': 36627140,
'Chile': 18314060,
'China': 1388251023,
'Colômbia': 49069267,
'Costa do Marfim':23869656,
'Croácia': 4207355,
'Cuba': 11486750,
'Chipre': 1189395
}
print('EXERCÍCIO 3:')
print("_"*60)
ordem = sorted(dicionário.items(), key = lambda item : item[1])
print(ordem)
print("_"*60)


