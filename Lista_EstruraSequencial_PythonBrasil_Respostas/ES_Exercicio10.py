#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#https://wiki.python.org.br/EstruturaSequencial

print("********************CALCULAR °C PARA °F*******************")
temperaturaC=float(input("DIGITE A TEMPERATURA °C: "))

temperaturaF=((temperaturaC*9//5)+32)

print("\n")
print("O VALOR ", temperaturaC,"°C EM °F ", temperaturaF)