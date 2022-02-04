from datetime import datetime

hora_atual=datetime.now().hour #importa a hora atual do computador

if hora_atual>=18:
    print("Boa noite!")
elif hora_atual>=12:
    print("Boa tarde!")
else:
    print("Bom dia!")
