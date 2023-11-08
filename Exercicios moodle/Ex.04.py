list = [1, 2, 3, 10, 22, 33, 44]

num = int(input("Digite um numero: "))


def ret_position(list, x):
    for i in range(len(list)):
        if list[i] == x:
            return i
    return -1


print(ret_position(list, num))
