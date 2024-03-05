"""
while True:  #loop infinito
    nome = input('Qual seu nome? ')
    print(f'Olá {nome}!')

print('Não será executada!')
"""
x = 0  #coluna

while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'({x},{y})')
        y += 1  #y = y + 1
    x += 1  #x = x + 1
print('Acabou!')
"""
while x < 10:
    if x == 3:
        x = x + 1
        break

    print(x)
    x = x + 1
#print('Acabou!')
"""

