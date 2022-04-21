media=0
for i in range(1,5):
    nota=float(input("Digite a sua {}ª nota: ".format(i)))
    media+=nota

media=media/4 #fora do laço for pois a nota não deve ser dividida 4 vezes
            #apenas a soma final de todas as notas deve ser dividida
print("A sua média é {:.1f}".format(media))