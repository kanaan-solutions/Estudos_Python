from cliente import Cliente


class Banco():
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    def inserir_cliente(self, cliete):
        self.clientes.append(cliete)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def auntenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if Cliente.conta not in self.contas:
            return False

        if Cliente.conta.agencia not in self.agencias:
            return False

        return True
