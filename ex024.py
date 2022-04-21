'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
com "SANTO"
'''
'''
#Este código não tá funcionando - ele só retorna o else
#Este código não diz se o nome da cidade COMEÇÃ com santo, apenas se ela tem santo no nome 
(em qualquer posição)
cit = str(input("Digite o nome da sua cidade: ")).upper()
print('SANTO' in cit or 'SANTA' in cit)
if 'SANTO' in cit is True or "SANTA" in cit is True: 
#ignora o "is" -> if 'SANTO' in cit -> já é automaticamente true
#if 'SANTO' in cit:
    #print(xxx)
    
    print("O nome da sua cidade possui o nome de um santo.")
else:
    print("O nome da sua cidade não possui o nome de um santo.")
'''
#cit=str(input("Digite o nome da sua cidade:")).upper().split().strip() -> São dá certo pois
#não dá pra tirar o espaçamento após o .split()

#split() dividiu a variável em diferentes caracteres
cit=str(input("Digite o nome da sua cidade:")).strip().upper().split()
#Se o primeiro caracter da variável for santo ou santa, vai aparecer na tela a mensagem
if cit[0]=="SANTO" or cit[0]=="SANTA":
    print("O nome da sua cidade é o nome de um santo")
else:
    print("O nome da sua cidade não é o nome de um santo")