from abc import ABC, abstractmethod

class IConta(ABC):
    @abstractmethod
    def consultar_conta():
        pass

    @abstractmethod
    def fazer_deposito():
        pass

    @abstractmethod
    def fazer_saque():
        pass

class Conta(IConta):
    def __init__(self,titular,cpf,agencia,n_conta,saldo):
        self.__ cpf = cpf 
        self.__agencia = agencia
        self.__n_conta = n_conta
        self.__saldo = saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf

    @property
    def agencia(self):
        return self.__agencia
    
    @agencia.setter
    def agencia(self,agencia):
        self.__agencia = agencia

    @property
    def n_conta(self):
        return self.__n_conta
    
    @n_conta.setter
    def n_conta(self,n_conta):
        self.__n_conta = n_conta

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo

# metodos da interface
def consultar_conta(self):
    print(f"Nome do titular da conta:{self.__titular}")
    print(f"CPF do titular da conta:{self.__cpf}")
    print(f"Agencia da conta:{self.__agencia}")
    print(f"Numero da conta:{self.__n_conta}")
    print(f"Saldo da conta:{self.__saldo:.2f}")

def fazer_deposito(self,valor):
    self.__saldo += valor
    return self.__saldo

def fazer_saque(self,valor):
    self.__saldo -= valor
    return self. __saldo