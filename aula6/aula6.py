"""
Iniciar com letra, pode conter números, separar_, letras minúsculas
"""

nome = 'Lucas'  #str
idade = 22  #int
altura = 1.80  #float
peso = 60
e_maior = idade > 18  #bool
data_1 = True
data_atual = 2022
imc = (peso / (altura * altura))

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Maioridade:',e_maior)
print(idade * altura)
print(nome,'tem', idade, 'anos e seu imc é:', imc)
