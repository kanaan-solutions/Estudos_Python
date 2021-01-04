nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")
altura = input("Qual sua altura? ")
peso = input("Qual seu peso? ")
ano_atual = 2020

idade = int(idade)
altura = float(altura)
peso = float(peso)

ano_nascimento = ano_atual - idade

IMC = peso / altura ** 2

print(f'Olá {nome}, você tem {idade} anos, '
      f'{altura} de altura, pesa {peso}, '
      f'seu ano nascimento foi em {ano_nascimento} e seu IMC é {IMC}')
