#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
#https://wiki.python.org.br/EstruturaSequencial

print("********************AREA DO QUADRADO*******************")
base=float(input("DIGITE A BASE DO QUADRDADO: "))
altura=float(input("DIGITE A ALTURA DO QUADRDADO:"))

area=base*altura
areaDobro=area*2

print("\n")
print("********************RESULTADO DA AREA DO QUADRADO*******************")
print("VALOR DA AREA DE BASE", base,"E ALTURA:", altura,"É: ", area)
print("VALOR DA AERA EM DOBRO: ", areaDobro)