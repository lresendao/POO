
nome = 'Luiz'
idade = 35
altura = 1.80
peso = 80
imc = peso / (altura ** 2)
ano_atual = 2022
ano_de_nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura}m de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_de_nascimento}.')
