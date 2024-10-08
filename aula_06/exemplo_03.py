nomes = []
medias = []
resp = "s"
while resp == "s":
    nomes.append(input("informe o nome do estudante: "))
    medias.append(float(input("informe a media do estudante: ")))
    resp = input("deseja continuar(s/n)? ")
for i in range(len(medias)):
    print(i,"-",nomes[i],"-" ,medias[i])
maior_media = max(medias)
pos = medias.index(maior_media)
print(f"{nomes[pos]}, voce possuia maior media.")
print(f"a media da truma é {(sum(medias)/len(medias)):1f}")
print(f"a maior media da turma é {max(medias)}")
print(f"a amplitude da media da turma é {max(medias)-min(medias)}")
medias.sort()
print(medias)