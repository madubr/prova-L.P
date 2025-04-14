"""#3. Você está organizando um evento e deseja que os seus convidados se
sintam importantes. Sendo assi, quando cada convidado chega ao local você
pergunta o nome dele e digita no computador. Então o nome dele é exibido em
um painel luminoso na entrada do salão. A mensagem que aparece é: "Seja
muito bem-vindo Fulano de Tal, onde Fulano de Tal é o nome da pessoa que
chegou.
Formato de entrada
O nome da pessoa, que pode conter até 120 caracteres
Formato de saída
O programa deve imprimir a mensagem "Seja muito bem-vindo Fulano de Tal"""
nome = input("digite o nome do convidado: ")

while len(nome) > 120:
    print("você digitou muitos caracteres")
    nome = input("digite o nome do convidado: ")

print(f"Seja muito bem-vindo: {nome}")