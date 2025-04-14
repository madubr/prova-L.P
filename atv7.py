"""#7. Faça um programa que leia uma string e dois caracteres. Troque todas as ocorrências do primeiro caracter pelo segundo. Exemplo: Seja a string "maracatu" e os caracteres 'a' e 'o', então a string ficará "morocotu".
Formato de entrada Você receberá 03 linhas.  Primeira linha: a string  Segunda linha: o primeiro caracter  Terceira linha: o segundo caracter A string possui no máximo 100 caracteres.
Formato de saída Imprima a palavra resultante da substituição dos caracteres na string original."""
palavra = input("digite uma palavra: ")

caracter = []

while len(palavra) > 100:
    print("você escrevreu muitos caracteres digite até [100]")
    palavra = input("digite uma palavra: ")


for i  in range(2):
    caractertemp = input(f"digite o {i+1}° caracter: ")
    caracter.append(caractertemp)

troca = palavra.replace(caracter[0],caracter[1])

print(troca)