"""#9. Escreva um programa leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.
Formato de entrada Contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.
Formato de saída Todos os inteiros entre x e y, um por linha"""
numerox = int(input("digite um numero: "))
numeroy = int(input("digite o outro numero: "))

if numerox > numeroy:
    numerox, numeroy = numeroy,numerox


for i in range(numerox + 1, numeroy):
    if i % 5 == 2 or i % 5 == 3:
        print(i)