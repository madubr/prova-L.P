"""#5. Serão dados n números correspondendo as notas da turma de alunos de uma escola. Escreva um programa que leia essas notas e calcule: - quantas estão mais de 10% acima da média. - quantas estão menos de 10% abaixo da média.
Formato de entrada Na primeira linha você receberá um número inteiro n, que representará a quantidade de alunos da turma. N <= 20000. Em seguida você receberá n números reais, um em cada linha, correspondendo as notas de cada aluno da turma.
Formato de saída Imprima na primeira linha da saída a média das notas formatada com duas casas decimais. Na segunda linha imprima quantas notas ficaram mais de 10% acima da média da turma. Na terceira linha imprima quantas notas ficaram menos de 10% abaixo da média da turma."""

vezes = int(input("digite a quantidade de alunos: "))
notas = []

for _ in range(vezes):
    nota = float(input("digite a nota"))
    notas.append(nota)

media = sum(notas) / vezes

acima = 0
abaixo = 0

for nota in notas:
    if nota > media * 1.10:
        acima += 1
    elif nota < media * 0.90:
        abaixo += 1

print(f"media da turma: {media:.2f}")
print(f"{acima} ficaram a cima de 10% da media")
print(f"{abaixo} ficaram a menos de 10% abaixo da media")


