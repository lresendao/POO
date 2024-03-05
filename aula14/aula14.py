#
#:s - Texto (strings)
#:d - Inteiros (int)
#:f - Números de ponto flutuante (float)
#.(numero)f - quantidade de casas decimais (float)
#(caracteres) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)
# > - Esquerda
# < - Direita
# ^ - Centro
"""
num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')"""

num_1 = 1
print(f'{num_1:0<10}')

num_2 = 3
print(f'{num_2:0>10}')

num_3 = 15
print(f'{num_3:0^10}')

nome = 'Lucas Resende'
nome_formatado = '{:@<15}'.format(nome)
print(nome_formatado)

nome2 = 'Lucas'
sobrenome = 'Resende'
nome_formatado2 = '{0} {1:@^30}'.format(nome2, sobrenome)
print(nome_formatado2)

nome3 = 'Bruno'
nome3 = nome3.ljust(20, '$')
print(nome3.lower())
print(nome3.upper())
print(nome3.title())