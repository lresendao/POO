"""
Calculadora com Loop
"""
while True:
    print()
    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    operador = input("Digite um operador: ")

    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Você precisa digitar dois números!")
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # operadores (+ - / *)
    if operador == '+':
        print(num_1 + num_2)
        sair = input('Deseja sair? [sim] ou [não] ')
        if sair == 'sim':
            break
        if sair == 'não':
            continue
    elif operador == '-':
        print(num_1 - num_2)
        sair = input('Deseja sair? [sim] ou [não] ')
        if sair == 'sim':
            break
        if sair == 'não':
            continue
    elif operador == '/':
        print(num_1 / num_2)
        sair = input('Deseja sair? [sim] ou [não] ')
        if sair == 'sim':
            break
        if sair == 'não':
            continue
    elif operador == '*':
        print(num_1 * num_2)
        sair = input('Deseja sair? [sim] ou [não] ')
        if sair == 'sim':
            break
        if sair == 'não':
            continue
    else:
        print('Operador inválido!')