print('Cafés disponíveis na máquina:  Café normal, Café expresso, Capuccino ou Mocaccino')

café_1 = ('Café normal') 
café_2 = ('Café expresso') 
café_3 = ('Capuccino') 
café_4 = ('Mocaccino') 


valor_café1 = 2.50
valor_café2 = 2.75
valor_café3 = 3.50
valor_café4 = 3.25

tipo_de_cafe = input('Digite café escolhido: ')
if tipo_de_cafe == café_1:
    print('Total a pagar:R$', valor_café1)
elif tipo_de_cafe == café_2:
    print('Total a pagar: R$', valor_café2)
elif tipo_de_cafe == café_3:
    print('Total a pagar: R$',valor_café3)
else:
    print('Total a pagar: R$',valor_café4)

valor_depositado = float(input('Quantia depositada para o pagamento: '))

def troco2(valor_depositado,valor_café3):
    print('o troco sera de: ', round(( valor_depositado - valor_café3),3))
    valor_depositado = valor_depositado - valor_café3
    print('serão utilizadas', int(valor_depositado), 'moedas de 1 real')
    valor_depositado = valor_depositado - int(valor_depositado)

if valor_depositado>=0.50:
    valor_depositado=valor_depositado-0.50
    print('sera usada 1 moeda de 50 centavos')
if valor_depositado>=0.25:
    valor_depositado=valor_depositado-0.25
    print('sera utilizada 1 moeda de 25 centavo')
if valor_depositado>=0.20:
    valor_depositado=valor_depositado-0.20
    print('serão utilizadas 2 moedas de 10 centavos')
if valor_depositado>=0.10:
    valor_depositado=valor_depositado-0.10
    print('sera utilizada 1 moeda de 10 centavos')
elif valor_depositado>=0.05:
    valor_depositado=valor_depositado-0.05
    print('sera utilizad 1 moeda de 5 centavos')
if valor_depositado>0:
    print('serão utilizadas', round(valor_depositado*100,1),'moedas de 1 centavo')



