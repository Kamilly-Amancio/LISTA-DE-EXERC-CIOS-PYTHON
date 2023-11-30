#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
#https://wiki.python.org.br/EstruturaSequencial

print("********************PESO DO PEIXE*******************")
pesoPeixe=float(input("DIGITE O PESO DO VALOR DO PEIXE: "))

multa=4.0
pesoRegulamento=50
excesso=0

excesso=pesoPeixe-pesoRegulamento
multaTotal=excesso+multa

if excesso>0:
    print("\n")
    print("VALOR DE MULTA: ", multa)
    print("VALOR DO EXCESSO DE PESO: ", excesso)
else:
    print("DENTRO DO LIMITE DE PESO! SEM MULTA")

