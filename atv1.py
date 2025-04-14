#1. Faça um programa que leia 3 números inteiros e os imprima em ordem crescente.
inteiro = []
for i in range(3):
    numero = int(input(f"digite o {i+1}° número: "))
    inteiro.append(numero)

inteiro.sort()
print(inteiro)

