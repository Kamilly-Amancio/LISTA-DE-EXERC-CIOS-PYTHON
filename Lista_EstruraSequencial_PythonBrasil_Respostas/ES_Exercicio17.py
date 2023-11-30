#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
#https://wiki.python.org.br/EstruturaSequencial

import math

def calcular_tinta(area):
    litros_necessarios = area / 6 * 1.1  # Adiciona 10% de folga
    latas_18l = math.ceil(litros_necessarios / 18)
    galoes_36l = math.ceil(litros_necessarios / 3.6)
    return litros_necessarios, latas_18l, galoes_36l

def calcular_preco(latas_18l, galoes_36l):
    preco_latas = latas_18l * 80
    preco_galoes = galoes_36l * 25
    return preco_latas, preco_galoes

def calcular_preco_misturado(latas_18l, galoes_36l):
    latas_necessarias = latas_18l
    galoes_necessarios = 0

    while galoes_necessarios * 3.6 < (latas_18l * 18 - latas_necessarias * 18):
        galoes_necessarios += 1

    preco_latas = latas_necessarias * 80
    preco_galoes = galoes_necessarios * 25
    return preco_latas, preco_galoes

area_a_pintar = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios, latas_18l, galoes_36l = calcular_tinta(area_a_pintar)
preco_latas, preco_galoes = calcular_preco(latas_18l, galoes_36l)
preco_latas_misturado, preco_galoes_misturado = calcular_preco_misturado(latas_18l, galoes_36l)

print("\nQuantidade de tinta necessária:")
print(f"Total de litros: {litros_necessarios:.2f}L")
print(f"Latas de 18L: {latas_18l}")
print(f"Galões de 3,6L: {galoes_36l}")

print("\nPreços:")
print(f"Para comprar apenas latas de 18 litros: R${preco_latas:.2f}")
print(f"Para comprar apenas galões de 3,6 litros: R${preco_galoes:.2f}")
print(f"Para misturar latas e galões: R${min(preco_latas_misturado, preco_galoes_misturado):.2f}")