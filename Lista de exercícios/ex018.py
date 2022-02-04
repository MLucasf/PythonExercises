vel=int(input("Qual é a velocidade da sua internet?"))/8 #mbps para MBps (megabit para megabyte)
tam=float(input("Qual é o tamanho do arquivo?"))
vel_down=tam/vel #mb/mbps
temp_min=vel_down/60 #transformar os segundos em minutos
temp_hor=temp_min/60
print("O tempo que você demorará para baixar o arquivo será de {:.1f}seg ou {:.1f}min ou {:.1f}hr".format(vel_down,temp_min,temp_hor))



