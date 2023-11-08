media = 0

tam = int(input("Quantidade de numeros: "))

vet_num = []


def read_num(vet_num, tam):
    for i in range(tam):
        num = float(input(f"digite o {i+1}º numero: "))
        vet_num.append(num)

    print("numeros lidos: ", vet_num)


def calc_media(media, tam, vet_num):
    soma = 0
    for i in range(len(vet_num)):
        soma = soma + vet_num[i]

    media = soma/tam
    print("A media sera: ", media)


read_num(vet_num, tam)

calc_media(media, tam, vet_num)
