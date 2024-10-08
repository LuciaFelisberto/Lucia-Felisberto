usuarios = ["Pedro","Maria","Duda","Dirceu","Elvis"]
senhas = ["123", "345", "567", "@@@###","8910"]
usuario = input("informe o nome de acesso ao sistema: ")
for i in range(len(usuarios)):
    if usuarios[i] == usuario:
        reso = "usuario encontrado"
        break
    else:
        resp = "usuario nao encontrado"
        print(resp)