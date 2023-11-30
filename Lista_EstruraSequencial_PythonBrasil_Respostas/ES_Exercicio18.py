#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
#https://wiki.python.org.br/EstruturaSequencial

def calcular_tempo_download(tamanho_arquivo, velocidade_internet):
    tamanho_arquivo_mb = tamanho_arquivo * 8
    tempo_segundos = tamanho_arquivo_mb / velocidade_internet
    tempo_minutos = tempo_segundos / 60

    return tempo_minutos

tamanho_arquivo = float(input("Informe o tamanho do arquivo para download (em MB): "))
velocidade_internet = float(input("Informe a velocidade do link de Internet (em Mbps): "))

tempo_download = calcular_tempo_download(tamanho_arquivo, velocidade_internet)

print(f"\nO tempo aproximado de download do arquivo é de {tempo_download:.2f} minutos.")
