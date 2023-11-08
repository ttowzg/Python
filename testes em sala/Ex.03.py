#repetição

frutas = ["uva", "maça", "banana", "pera"]
print(frutas[1])
print(frutas[1:3])
print(frutas[:])
print(frutas[:3])
print(frutas[-1])
print(frutas[0:2] + frutas[2:3])
print(frutas[1][2]) #acesso como matriz

frutas.append("kiwi")
frutas.pop(1)
frutas.remove("uva")
frutas.insert(0,158)
frutas += ["manga"]
print(frutas)

print("pera" in frutas)
print(frutas.index("pera"))

#------------------------------#
#      repeticão       #

#for

for i in range(len(frutas)): #----------> range (inicio, tamanho, incremento)
    print(frutas[i])

for fruta in frutas:
    print(fruta)




