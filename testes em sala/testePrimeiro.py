altura = float(input("informe a altura: "))

print(altura)

if(altura >= 1.8):
    print("alto")
elif altura < 1.85 and altura >= 1.6:
    print("medio")
else:
    print("baixo")
    if altura < 1.4:
        print("anão ou crinça")