hora = input('Que horas são? ')

if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print("Digite um horário entre 0 e 23.")
    if hora >=0 and hora <= 11:
        print("Bom Dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa Tarde!")
    elif hora >= 18 and hora <= 23:
        print("Boa Noite!")
else:
    print("Digite um horário válido!")

