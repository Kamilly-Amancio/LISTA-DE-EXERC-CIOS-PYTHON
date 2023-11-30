#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).
#https://wiki.python.org.br/EstruturaSequencial

print("********************CALCULAR °F PARA °C*******************")
temperaturaF=float(input("DIGITE A TEMPERATURA °F: "))

temperaturaC=(5*((temperaturaF-32)//9))

print("\n")
print("O VALOR ", temperaturaF,"°F EM °C ", temperaturaC)