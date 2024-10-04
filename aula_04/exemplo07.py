try:
    idade = int (input("informar a idade: "))
    tempo_trabalho = int (input("informar o tempo trabalhado: "))
except ValueError:
    print("verifique os dados informado")
else:
    if idade >= 65:
        print("esta apto a aposentar:")
    elif tempo_trabalho >= 30:
        print("esta inapto aposentar:")
    elif idade >= 60 and tempo_trabalho >= 25:
        print("voce esta apto")
    else:
        print("voce esta inapto")

