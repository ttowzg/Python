"""Escreva um programa Python que receba o salario de um funcionario e calcule o seu imposto de renda. 
O imposto de renda e calculado da seguinte forma: o salario e multiplicado
por uma porcentagem (aliquota) de acordo com faixas pre-estabelecidas. Desse valor e
deduzido um valor fixo, tambem de acordo com faixas pre-estabelecidas. """
print("----- Bem Vindo -----")
sal_entrada = int(input("Digite seu salario para o calculo: "))

if sal_entrada <= 1903.98:
    sal_final = sal_entrada

elif sal_entrada >= 1903.99 and sal_entrada <= 2826.65:
    sal_final = (sal_entrada * 0.075) - 142.8

elif sal_entrada >= 2826.66 and sal_entrada <= 3751.05:
    sal_final = (sal_entrada * 0.15) - 354.80

elif sal_entrada >= 3751.06 and sal_entrada <= 4664.68:
    sal_final = (sal_entrada * 0.225) - 636.13

else:
    sal_final = (sal_entrada * 0.275) - 869.36

print("----- Voce tera que pagar -----")
print("---> ", sal_final)
