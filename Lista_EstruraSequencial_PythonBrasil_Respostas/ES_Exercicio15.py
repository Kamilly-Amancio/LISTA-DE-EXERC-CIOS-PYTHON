#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#   + Salário Bruto : R$
#   - IR (11%) : R$
#   - INSS (8%) : R$
#   - Sindicato ( 5%) : R$
#   = Salário Liquido : R$ (Obs.: Salário Bruto - Descontos = Salário Líquido.)
#https://wiki.python.org.br/EstruturaSequencial

print("********************SALÁRIO*******************")
horasTrabalhadas=int(input("DIGITE AS HORAS TRABALHAS: "))
valorHoras=float(input("DIGITE O VALOR QUE GANHA POR HORAS: "))

salarioBruto=horasTrabalhadas*valorHoras
#IR VALOR DESCONTADO
irValor=0.11
irTotal=(salarioBruto-irValor)

#INSS VALOR DESCONTADO
inssValor=0.08
inssTotal=(salarioBruto-inssValor)

#SINDICATO VALOR DESCONTO
sindicatoValor=0.05
sindicatoTotal=(salarioBruto-sindicatoValor)

salarioLiquido=((irTotal+inssTotal+sindicatoTotal)-salarioBruto)

print("\n")
print("+  Salário Bruto: R$", salarioBruto)
print("-  IR (11%): R$", irTotal)
print("-  INSS (8%): R$", inssTotal)
print("-  SINDICATO (5%): R$", sindicatoTotal)
print("= Salário Líquido: R$", salarioLiquido)