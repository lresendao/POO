
nome = input("Qual seu nome? ")
idade = input("Qual a sua idade? ")
idade = int(idade)
idade_muito_jovem = 20
idade_muito_velho = 30
#Limite para pegar empréstimo

if idade >= idade_muito_jovem and idade <= idade_muito_velho:
    print(f'{nome} pode pegar o emprestimo')
else:
    print(f'{nome} Não pode pegar o empréstimo.')