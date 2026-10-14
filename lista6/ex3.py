class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def mostrar_saldo(self):
        return self.saldo


conta_ignacio = ContaBancaria("Ignacio", 1000)

conta_ignacio.depositar(500)
conta_ignacio.depositar(200)

conta_ignacio.sacar(300)

print(conta_ignacio.mostrar_saldo())
