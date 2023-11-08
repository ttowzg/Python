#Escreva uma função que recebe um array
#e retorna uma soma de seus elementos

def soma_arr (arr):
    soma = 0

    for i in range(len(arr)):
        soma += arr[i]
    return soma

if __name__ == "__main__":
    print("digite 10 numeros: ")

    a = []

    for i in range(10):
    a.append(int(input("numero: "))) 


    print("A soma sera: ")
    print(soma_arr(a))

