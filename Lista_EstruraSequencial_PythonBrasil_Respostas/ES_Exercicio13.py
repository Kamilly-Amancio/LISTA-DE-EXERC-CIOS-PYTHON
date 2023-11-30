#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
#https://wiki.python.org.br/EstruturaSequencial

print("********************PESO IDEAL 'H' OU 'M'*******************")
altura=float(input("DIGITE A SUA ALTURA: "))
sexo=eval(input("SEXO 'M' - MULHER OU 'H'-  HOMEM: "))

if sexo=='m' and sexo=='M':
    calculoMulher=((62.1*altura)-44.7)
    print("O PESO IDEAL DA MULHER É: ", calculoMulher)
else:
    calculoHomem=((72.7*altura)-58)
    print("O PESO IDEAL DA HOMEM É: ", calculoHomem)