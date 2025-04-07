class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            raise ValueError("El monto a depositar debe ser mayor que cero.")

    def retirar(self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
        else:
            raise ValueError("Monto inválido para retirar.")

    def consultar_saldo(self):
        return self.__saldo

    def consultar_titular(self):
        return self.__titular
