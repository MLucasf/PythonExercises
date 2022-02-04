nota_final=0
for i in range(0,4):
    nota=float(input("Digite a sua {}ª nota: ".format(i+1)))
    nota_final+=nota
media=nota_final/4
if media>=9.5: #o menos abrangente (apenas notas superiores a 9.5
    print("Muitos parabéns! A sua média foi {:.1f} e você foi aprovado com distinção!".format(media))
elif media>=7: #o mais abrangente (notas de 7 até a condição do mais abrangente)
    print("Parabéns, sua média foi {:.1f} e você está aprovado".format(media))
else: #exceções (notas que não se encaixam no statement mais abrangente e menos abrangente)
    print("infelizmente você não foi aprovado. A sua média foi {:.1f}".format(media))

