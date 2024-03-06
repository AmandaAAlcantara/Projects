print('Petshop')
RG = (input('Insira seu RG: '))
nome_do_cachorro = (input('Insira nome do cachorro: '))
raça = (input('Insira raça: '))
idade = int(input('Insira idade do cachorro (anos): '))
peso = float(input('Peso (Kg) do cachorro: '))


if peso < 8:
    print('ORÇAMENTO: Dados de entrada (','RG=',RG,', Nome do Cachorro=',nome_do_cachorro,', Raça=',raça,', Idade=',idade,'anos, Peso=',peso,'Kg). Preço de hospedagem por semana = R$ 50.00.')      
elif 8 <= peso <= 15:
    print('ORÇAMENTO: Dados de entrada (','RG=',RG,', Nome do Cachorro=',nome_do_cachorro,', Raça=',raça,', Idade=',idade,'anos, Peso=',peso,'Kg). Preço de hospedagem por semana = R$ 70.00.')
elif  15 < peso <= 40:
    print('ORÇAMENTO: Dados de entrada (','RG=',RG,', Nome do Cachorro=',nome_do_cachorro,', Raça=',raça,', Idade=',idade,'anos, Peso=',peso,'Kg). Preço de hospedagem por semana = R$ 100.00.') 
else: 
    print('ORÇAMENTO: Dados de entrada (','RG=',RG,', Nome do Cachorro=',nome_do_cachorro,', Raça=',raça,', Idade=',idade,'anos, Peso=',peso,'Kg). Preço de hospedagem por semana = R$ 125.00.')


