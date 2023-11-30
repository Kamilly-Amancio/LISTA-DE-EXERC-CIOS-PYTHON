#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
#https://wiki.python.org.br/EstruturaSequencial

print("********************CALCULO SALÁRIO NO MÊS*******************")
horasTrabalhadas=int(input("DIGITE AS HORAS TRABALHAS: "))
valorHoras=float(input("DIGITE O VALOR QUE GANHA POR HORAS: "))

valorTotal=horasTrabalhadas*valorHoras

print("\n")
print("********************RESULTADO DO CALCULO SALÁRIO NO MÊS*******************")
print("TRABALHOU ", horasTrabalhadas,"HORAS E O VALOR DAS HORAS SÃO R$ ", valorHoras,"LOGO O TOTAL DO SALÁRIO NO REFERIDO MÊS É R$", valorTotal)
