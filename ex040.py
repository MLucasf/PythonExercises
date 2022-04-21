'''Crie um programa que leia duas notas de um aluno e calcule a sua média,
mostrando uma mensagem no final de acordo com a média atingida:
- média abaixo de 5.0: reprovado
- média entre 5.0 e 6.9: recuperação
- média 7.0 ou superior: aprovado
- média 9.5 ou superior: aprovado com méritos '''
n1=float(input("Digite a sua primeira nota:"))
n2=float(input("Digite a sua segunda nota:"))
n3=float(input("Digite a sua terceira nota:"))
n4=float(input("Digite a sua quarta nota:"))
media=(n1+n2+n3+n4)/4
if media<5:
    print("\033[31mSua média foi {:.1f}, e por ser menor que 5 você está reprovado\033[m".format(media))
elif media>=5 and media<7:
    print("\033[35mSua média foi {:.1f} e por ser menor que 7 você está de recuperação\033[m".format(media))
elif media>=7 and media<9.5:
    print("\033[4;32mSua média foi {:.1f} e você está aprovado. Parabéns!\033[m".format(media))
else:
    print("\033[1;36mParabéns, sua média foi {:.1f} e você foi aprovado com méritos!\033[m".format(media))