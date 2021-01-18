from banco import Banco
from cliente import Cliente
from conta import ContaPoupanca, ContaCorrente

banco = Banco()

cliente1 = Cliente("André", 22)
cliente2 = Cliente("Alice", 24)
cliente3 = Cliente("Diana", 52)

conta1 = ContaPoupanca(1111, 527490, 0)
conta2 = ContaCorrente(2222, 254216, 0)
conta3 = ContaPoupanca(3547, 347685, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

if banco.auntenticar(cliente2):
    cliente2.conta.depositar(250)
    cliente2.conta.sacar(10)
else:
    print("Cliente não autenticado")
