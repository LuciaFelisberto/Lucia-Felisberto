nome = input("informe o nome do estudante: ")
n1 = float(input("informe a primeira nota: "))
n2 = float(input("informe a segunda nota: "))
media = (n1 + n2) / 2
print(media)
if media >=70:
    print(f"{nome}, voce esta aprovado, pois a sua media foi {media: .2f}")
elif media>=30 and media<70:
     print(f"{nome}, voce esta e recuperaçao, pois a sua media foi {media: .2f}")
elif media <=30:
     print(f"{nome}, voce esta reprovado, pois a sua media foi {media: .2f}")
