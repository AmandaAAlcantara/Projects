import math

print('<1> sen (x)')
print('<2> cos(x)') 
print('<3> tg(x)') 
print('<4> cossec(x)')
print('<5> sec(x)') 
print('<6> cotg(x)') 
print('<0> Sair do programa')

opção_desejada = float(input('Digite a opção desejada: '))
opção1 = float(('1'))
opção2 = float(('2'))
opção3 = float(('3'))
opção4 = float(('4'))
opção5 = float(('5'))
opção6 = float(('6'))
opção0 = float(('0'))


if opção_desejada == opção1:
    resultado1 = float(input('Digite o valor do angulo (graus) para cálculo: '))
    rad = (resultado1*math.pi)/180
    print('Resultado da função é:',math.sin(rad))
elif opção_desejada == opção2:
    resultado2 = float(input('Digite o valor do angulo (graus) para cálculo: '))
    rad = (resultado2*math.pi)/180
    print('Resultado da função é:',math.cos(rad))
elif opção_desejada == opção3:
    resultado3 = float(input('Digite o valor do angulo (graus) para cálculo: '))
    rad = (resultado3*math.pi)/180
    print('Resultado da função é:',math.tan(rad))
elif opção_desejada == opção4:
    resultado4 = float(input('Digite o valor do angulo (graus) para cálculo: '))
    rad = (resultado4*math.pi)/180
    cossec = 1/math.sin(rad)
    print('Resultado da função é:',cossec)
elif opção_desejada == opção5:
    resultado5 = float(input('Digite o valor do angulo (graus) para cálculo: '))
    rad = (resultado5*math.pi)/180
    sec = 1/math.cos(rad)
    print('Resultado da função é:',sec)
elif opção_desejada == opção6:
    resultado6 = float(input('Digite o valor do angulo (graus) para cálculo: '))
    rad = (resultado6*math.pi)/180
    cotg = 1/math.tan(rad)
    print('Resultado da função é:',cotg )
elif opção_desejada == opção0:
    resultado0 = print('Encerrando o programa')
else:
    print('Erro, número digitado não está entre 0 e 6')

    


