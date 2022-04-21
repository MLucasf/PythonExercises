altura=int(input("Qual é a sua altura, em centímetros?"))
altura=altura/100
sex=str(input("Qual é o seu sexo? [M/F]")).strip().upper()
if sex=="M":
    peso_ideal=72.7*altura-58
elif sex=="F":
    peso_ideal=62.1*altura-44.7
else:
    print("Essa não é uma opção válida.")

print("O seu peso ideal, sabendo que a sua altura é {:.2f}m, é {:.1f}kg".format(altura,peso_ideal))