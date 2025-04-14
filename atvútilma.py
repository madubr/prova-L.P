"""#10. Faça um programa que leia n números inteiros dados e os imprima: 
a) na ordem inversa dos números dados b) ordenado em ordem decrescente"""


numeros = []

for i in range(4):
    numero = int(input(f"digite o {i+1}° número: "))
    numeros.append(numero)

print("\nOrdem inversa: ")
for numero in reversed(numeros):
    print(numero)


print("\nOrdem decrescente: ")
for numero in sorted(numeros,reverse=True):
    print(numero)
