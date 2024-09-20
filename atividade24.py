# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.



contador = 0
soma = 0
while True:
    num = float(input("digite os números para calcular as médias: "))
    if num == -1:
        break 
    soma += num
    contador += 1
    if contador > 0:
        media = soma/contador
print(media)
    