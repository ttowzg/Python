#condicionais

# escreva um programa que le 3 lados 
# de um triangulo e informe se é 
# equilatero, isoscelos ou escaleno

lado1 = int(input("informe a altura do lado 1: "))
lado2 = int(input("informe a altura do lado 2: "))
lado3 = int(input("informe a altura do lado 3: "))

if lado1 + lado2 >= lado3 or lado1 + lado3 >= lado2 or lado2 + lado3 >= lado1:
    print("É triangulo, então:") 


if lado1 == lado2 and lado2 == lado3:
    print("Equilatero")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("Escaleno")
else:
    print("Isóceles")


