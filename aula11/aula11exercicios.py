
usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'lucao'
senha_bd = '123456'

if usuario == usuario_bd and senha == senha_bd:
    print('Você está logado no sistema.')
else:
    print('Usuário ou Senha inválidos.')