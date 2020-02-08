class Conta:

    # Construtor Python
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Property(Getters)
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular.title()

    @property
    def saldo(self):
        return self.__saldo

    # Mesma coisa que o trecho de código abaixo
    # def get_limite(self):
    # return self.__limite
    @property
    def limite(self):
        return self.__limite

    # Setters / Propriedades
    # Mesma coisa do cód das linhas 36 à 38
    # def set_titular(self, titular):
    # self.__titular = titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do Titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if (self.__verifica_saldo(valor)):
            self.__saldo -= valor
        else:
            print("Limite insuficiente")

    def transferir(self, valor, destino):
        if (self.__verifica_saldo(valor)):
            self.sacar(valor)
            destino.depositar(valor)
        else:
            print("Limite insuficiente")

    def __verifica_saldo(self, valor):
        disponivel = self.__saldo + self.__limite
        return valor <= disponivel

    @staticmethod
    def cod_banco():
        return "001"

    @staticmethod
    def cod_bancos():
        return {'BB':'001', 'Caixa': '104', 'Bradesco': '237'}