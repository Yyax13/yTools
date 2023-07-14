def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media


nota1 = input("nota 1:  ")
nota2 = input("nota 2:  ")
nota3 = input("nota 3:  ")
nota4 = input("nota 4:  ")
notas = [nota1, nota2, nota3, nota4]
media = calcular_media(notas)
print("A média é:", media)
