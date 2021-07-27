
class Conta():
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        #print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_sacar):
        limite = self.__limite + self.__saldo
        return limite >= valor_sacar
    
    def saca(self, valor):        
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('Valor solicitado excede o limite máximo!')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        print(self.__saldo)

    @property
    def titular(self):
        return self.__titular.title()

    @property
    def limite(self):
        print(self.__limite)

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
