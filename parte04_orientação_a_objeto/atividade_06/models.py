
from abc import ABC, abstractmethod

# --- INTERFACE ---
class IConta(ABC):
    @abstractmethod
    def consultar_dados(self) -> None:
        pass

    @abstractmethod
    def gerar_extrato(self) -> None:
        pass

    @abstractmethod
    def depositar(self, valor: float) -> float:
        pass

    @abstractmethod
    def sacar(self, valor: float) -> float:
        pass


# --- CLASSE PESSOA ---
class Pessoa:
    def __init__(self, nome: str, cpf: str):
        self.nome: str = nome
        self.cpf: str = cpf

    def __str__(self) -> str:
        return f"Nome: {self.nome} | CPF: {self.cpf}"


# --- CLASSE CONTA (Implementa IConta) ---
class Conta(IConta):
    def __init__(self, titular: str, agencia: str, n_conta: str, saldo: float, pessoa: Pessoa):
        self.titular: str = titular
        self.agencia: str = agencia
        self.n_conta: str = n_conta
        self.saldo: float = saldo
        self.pessoa: Pessoa = pessoa # Relacionamento "possui" Pessoa

    def consultar_dados(self) -> None:
        print(f"--- DADOS DA CONTA ---")
        print(f"Agência: {self.agencia}")
        print(f"Número da Conta: {self.n_conta}")
        print(f"Titular (Conta): {self.titular}")
        print(f"Proprietário: {self.pessoa}")
        print(f"Saldo Atual: R$ {self.saldo:.2f}")

    def gerar_extrato(self) -> None:
        nome_arquivo = f"extrato_{self.n_conta}.txt"
        conteudo = (
            f"=== EXTRATO BANCÁRIO ===\n"
            f"Agência: {self.agencia}\n"
            f"Conta: {self.n_conta}\n"
            f"Titular: {self.titular}\n"
            f"CPF: {self.pessoa.cpf}\n"
            f"------------------------\n"
            f"Saldo Disponível: R$ {self.saldo:.2f}\n"
            f"========================\n"
        )
        try:
            with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
                arquivo.write(conteudo)
            print(f"Extrato gerado com sucesso no arquivo: {nome_arquivo}")
        except Exception as e:
            print(f"Erro ao gerar o arquivo de extrato: {e}")

    def depositar(self, valor: float) -> float:
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado.")
        else:
            print("Valor de depósito inválido.")
        return self.saldo

    def sacar(self, valor: float) -> float:
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")
        return self.saldo
