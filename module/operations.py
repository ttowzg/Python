def find_min(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min

a = [6, 8, 11, 4, 7]

print(find_min(a))

def find_max(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

print(find_max(a))

max = find_max(a)
min = find_min(a)

print(f"min: {min} max: {max}") # f pra formatar, mistura string e codigo (?)

#-------------------------------#

def soma_arr (arr):
    soma = 0

    for i in range(len(arr)):
        soma += arr[i]
    return soma
"""
print("digite 10 numeros: ")

a = []

for i in range(10):
    a.append(int(input("numero: "))) 


print("A soma sera: ")
print(soma_arr(a))
    """