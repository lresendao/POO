username = input("Digite o seu nome de usuário. ")

if len(username) <= 4:
    print("Seu nome é curto")
elif len(username) >= 5 and len(username) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muiIto grande")