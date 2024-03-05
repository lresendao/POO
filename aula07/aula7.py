nome = 'Lucas'  #str
idade = 22  #int
altura = 1.80  #float
peso = 60
e_maior = idade > 18  #bool
data_1 = True
data_atual = 2022
imc = (peso / (altura * altura))

print(f'{nome} tem {idade} anos de idade e seu imc é: {imc}')
print(f'{nome} tem {idade} anos de idade e seu imc é: {imc:.2f}')
print('{} tem {} anos de idade e seu imc é: {:.2f}'.format(nome,idade,imc))
print('{0} tem {1} anos de idade e seu imc é: {2}'.format(nome,idade,imc))
print('{n} tem {i} anos de idade e seu imc é: {im}'.format(n = nome,i = idade,im = imc))

#também posso mudar a ordem no padrão format.

