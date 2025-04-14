"""#4. Faça um programa que dado um número indique se ele é um primo ou não.
Obs: Para cada número lido você deve imprimir “Número não é Primo” caso o
número não seja primo ou “Número Primo” caso seja."""
numero = int(input("digite um numero: "))

if numero <= 1:
    print("numero não é primo")
else:
    ePrimo = True
    for i in range (2,numero):
        if numero % i == 0:
            ePrimo = False
            break

if ePrimo:
    print("numero primo")
else:
    print("numero não é primo")