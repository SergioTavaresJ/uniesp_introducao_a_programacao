# Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. 
# Depois:Imprima o resultado da soma de todos os valores da matriz no terminal;
# E, crie uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

from random import randint

matriz = []

for l in range(10):
    linha = []
    for c in range(10):
        linha.append(randint(1,15))
    matriz.append(linha)

soma = 0

for linha in matriz:

    for coluna in linha:
        soma += coluna

print(matriz)
print(f"A soma de todos os valores da matriz é: {soma}")

matrizb = []

for l in range(0, len(matriz)):
    list = []
    for c in range(0, len(matriz[l])):
        mult = matriz[l][c] * 3
        matrizb.append(mult)
    matrizb.append(list)

print(matrizb)
