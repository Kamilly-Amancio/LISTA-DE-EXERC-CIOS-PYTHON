#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
#https://wiki.python.org.br/EstruturaSequencial

print("********************PESO IDEAL*******************")
altura=float(input("DIGITE A SUA ALTURA: "))

calculoPesoIdeal=((72.7*altura)-58)

print("\n")
print("********************RESULTADO PESO IDEAL*******************")
print("PESO IDEAL", calculoPesoIdeal)

