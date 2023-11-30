#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
#https://wiki.python.org.br/EstruturaSequencial

import math

print("********************LOJA DE TINTAS*******************")
area=float(input("DIGITE O TAMANHO EM METROS QUADRDADOS DA AREA: "))

valor=80.00
totalPreco=0
capacidadeLitro=3
capacidadeLata=18

if area<240:
    valor=valor
    print("\n")
    print("PRECISA DE MENOS QUE UMA LATA DE TINTA")
else:
    litros_necessarios = area / capacidadeLitro
    latas_necessarias = math.ceil(litros_necessarios / capacidadeLata)
    preco_total = latas_necessarias * valor

    print(f"TOTAL DE LATAS NECESSARIAS: ", latas_necessarias)
    print(f"\n PREÇO TOTAL: ",preco_total)

    

