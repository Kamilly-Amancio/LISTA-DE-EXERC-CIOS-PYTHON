#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
#https://wiki.python.org.br/EstruturaSequencial


print("********************PROGRAMA SITUAÇÕES A , B E C*******************")
numero1=int(input("DIGITE O PRIMEIRO NUMERO: "))
numero2=int(input("DIGITE O SEGUNDO NUMERO: "))
numero3=float(input("DIGITE O TERCEIRO NUMERO: "))

situacaoA=(numero1*(numero2/2))
situacaoB=((numero1*3)+numero3)
situacaoC=(numero3**2)

print("\n")
print("********************PROGRAMA SITUAÇÕES A , B E C*******************")
print("SITUAÇÃO A: ", situacaoA)
print("SITUAÇÃO B: ", situacaoB)
print("SITUAÇÃO C: ", situacaoC)