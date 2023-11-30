#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
#https://wiki.python.org.br/EstruturaSequencial

print("********************MÉDIA DAS NOTAS*******************")
nota1=float (input("DIGITE A PRIMEIRA NOTA:"))
nota2=float (input("DIGITE A SEGUNDA NOTA:"))
nota3=float (input("DIGITE A TERCEIRA NOTA:"))
nota4=float (input("DIGITE A QUARTA NOTA:"))

media=((nota1+nota2+nota3+nota4)/4)

print("\n")

print("********************RESULTADO MÉDIA DAS NOTAS*******************")
print("A MÉDIA DAS NOTAS 1: ", nota1,"NOTA 2: ", nota2,"NOTA 3:", nota3,"NOTA 4: ", nota4,"É: ", media)
