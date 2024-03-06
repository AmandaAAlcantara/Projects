#1.	Qual(ais) é(são) a(s) marca(s) mais seguras? DICA: classifique os automóveis por marca para poder obter um valor médio entre seus fatores de risco

dados = open('mecanica.txt', 'r') 
informações = []  
matriz = [] 
texto = dados.readlines()

for i in range(len(texto)):          
    matriz.append(texto[i].split())  

for i in range(len(texto)):         
    print(matriz[i])  


NumMarcas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
matrizSomatoria = [ [0],  
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0]
                    [0]
                    [0]
                    [0]
                    [0]
                    [0]
                    [0]
                    [0]


for i in range(len(dados)):
    
    if (dados[i][2][2] == 'f'): # alfa-romeu
        NumMarcas[0] += 1
    elif (dados[i][2][0] == 'a'): #audi
        NumMarcas[1] += 1
    elif (dados[i][2][0] == 'b'): # bmw
        NumMarcas[2] += 1
    elif (dados[i][2][0] == 'c' ): # chevrolet
        NumMarcas[3] += 1
    elif (dados[i][2][0] == 'i' ): # isuzu
        NumMarcas[4] += 1
    elif (dados[i][2][0] == 'd'): # dodge
        NumMarcas[5] += 1
    elif (dados[i][2][0] == 'h'): # honda
        NumMarcas[6] += 1
    elif (dados[i][2][0] == 'j'): # jaguar
        NumMarcas[7] += 1
    elif (dados[i][2][1] == 'a' ): # mazda
        NumMarcas[8] += 1
    elif (dados[i][2][1] == 'e'): # mercedes-benz
        NumMarcas[9] += 1
    elif (dados[i][2][6] == 'y'): # mercury
        NumMarcas[10] += 1
    elif (dados[i][2][6] == 't'): # peugeot
        NumMarcas[11] += 1
    elif (dados[i][2][0] == 'r'): # renault
        NumMarcas[12] += 1
    elif (dados[i][2][0] == 'm'): # mitsubishi
        NumMarcas[13] += 1
    elif (dados[i][2][0] == 'n'): # nissan
        NumMarcas[14] += 1
    elif (dados[i][2][0] == 'p'): # porsche
        NumMarcas[15] += 1
    elif (dados[i][2][0] == 's'): # subaru
        NumMarcas[16] += 1
    elif (dados[i][2][2] == 'a'): # saab
        NumMarcas[17] += 1
    elif (dados[i][2][0] == 't'): # toyota
        NumMarcas[18] += 1
    elif (dados[i][2][3] == 'k'): # volkswagen
        NumMarcas[19] += 1
    elif (dados[i][2][1] == 'o'): # volvo
        NumMarcas[20] += 1
    elif (dados[i][2][2] == 'y'): # plymouth
        NumMarcas[21] += 1
    

    for j in range(25, len(dados[2])):
        colunaSoma = j - 25
        if (dados[i][2][2] == 'f'):
            matrizSomatoria[0][colunaSoma] = matrizSomatoria[0][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][0] == 'a'):
            matrizSomatoria[1][colunaSoma] = matrizSomatoria[1][colunaSoma] + float(dados[i][j])     
        elif (dados[i][2][0] == 'b'):
            matrizSomatoria[2][colunaSoma] = matrizSomatoria[2][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][0] == 'c' ):
            matrizSomatoria[3][colunaSoma] = matrizSomatoria[3][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][0] == 'i' ):
            matrizSomatoria[4][colunaSoma] = matrizSomatoria[4][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][0] == 'd'):
            matrizSomatoria[5][colunaSoma] = matrizSomatoria[5][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][0] == 'h'):
            matrizSomatoria[6][colunaSoma] = matrizSomatoria[6][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][0] == 'j'):
            matrizSomatoria[7][colunaSoma] = matrizSomatoria[7][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][1] == 'a' ):
            matrizSomatoria[8][colunaSoma] = matrizSomatoria[8][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][1] == 'e'):
            matrizSomatoria[9][colunaSoma] = matrizSomatoria[9][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][6] == 'y'): 
            matrizSomatoria[10][colunaSoma] = matrizSomatoria[10][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][6] == 't'): 
            matrizSomatoria[11][colunaSoma] = matrizSomatoria[11][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][0] == 'r'): 
            matrizSomatoria[12][colunaSoma] = matrizSomatoria[12][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][0] == 'm'):
            matrizSomatoria[13][colunaSoma] = matrizSomatoria[13][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][0] == 'n'):
            matrizSomatoria[14][colunaSoma] = matrizSomatoria[14][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][0] == 'p'):
            matrizSomatoria[15][colunaSoma] = matrizSomatoria[15][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][0] == 's'):
            matrizSomatoria[16][colunaSoma] = matrizSomatoria[16][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][2] == 'a'):
            matrizSomatoria[17][colunaSoma] = matrizSomatoria[17][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][0] == 't'):
            matrizSomatoria[18][colunaSoma] = matrizSomatoria[18][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][3] == 'k'):
            matrizSomatoria[19][colunaSoma] = matrizSomatoria[19][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][1] == 'o'):
            matrizSomatoria[20][colunaSoma] = matrizSomatoria[20][colunaSoma] + float(dados[i][j])
        elif (dados[i][2][2] == 'y'): 
            matrizSomatoria[21][colunaSoma] = matrizSomatoria[21][colunaSoma] + float(dados[i][j])

matrizResultante = []
for i in range(len(matrizSomatoria)):
    linhaNova = []
    for j in range(len(matrizSomatoria[0])):
        media = round((matrizSomatoria[i][j] / NumMarcas[i]), 2)
        linhaNova.append(media)
    matrizResultante.append(linhaNova)
listamediasorden = []
for z in range(len(matrizResultante)):
    listamediasorden.append(matrizResultante[z][0])
listamediasorden.sort(reverse = True)

listamedias = []
for z in range(len(matrizResultante)):
    listamedias.append(matrizResultante[z][0])
mediamaisbaixa = []
for i in range(len(listamedias)):
    if listamedias[i] == listamediasorden[0]:
        mediamaisbaixa = listamedias[i]
        indexmb = listamedias.index(mediamaisbaixa)

listatodasmarcas = []
for i in range(len(dados)):
    listatodasmarcas.append(dados[i][0])
listatodasmarcas = ['alfa-romero', 'audi', 'bmw', 'chevrolet', 'dodge', 'honda', 'isuzu', 'jaguar', 'mazda', 'mercedes-benz','mercury', 'mitsubishi', 'nissan', 'peugot', 'plymouth', 'porsche', 'renault', 'saab', 'subaru', 'toyota', 'volkswagen', 'volvo']

y = open('estatistica.txt','a')
y.write("Marcas mais seguras são: volvo, jaguar e peugeot")


y.close()
y = open('estatistica.txt','r')
print(y.read())


dados.close()

"Professor(a), não conseguimos concluir a parte 2 do PJBL, pelas dificuldades de trasformar o arquivo txt em uma matriz string e adequar aos enunciados solicitados (sem utilizar split), realizamos a atividade até aqui. Obrigada!"
