from abc import ABC,  abstractclassmethod, abstractproperty
from datetime import datetime
class Cliente: 
    def __init__(self, endereço):
        self.endereço = endereço
        self.conta = []

    def Iniciar_Transação(self, conta, transação):
        transação.registrar(conta)

    def add_Conta(self, conta):
        self.contas.append(conta)

class Pessoa_Física(Cliente):
    def __init__(self, nome, data_de_nascimento, cpf, endereço):
        super().__init__(endereço)
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._histórico = histórico()

        @classmethod 
        def nova_conta (cls, cliente, numero):
            return cls(cliente, numero)
        @property
        def saldo(self):
            return self._saldo
        @property
        def agencia(self):
            return self._agencia
        @property
        def numero(self):
            return self._numero
        @property
        def histórico(self):
            return self._histórico
        
        def sacar (self, valor):
            saldo = self.saldo
            excedeu_saldo = valor > saldo
            if excedeu_saldo:
                print ("Falha, saldo insuficiente!")
            elif valor > 0:
                self.saldo -= valor
                print ("Saque bem sucedido!")
                return True
            else:
                print ("Falha!")
                return False
        def depositar (self, valor):
            if valor > 0:
                self.saldo += valor
                print ("Depósito bem sucedido!")
            else:
                print ("Valor Inválido!")
                return False
            return True

class Conta_Corrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saque = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len (
            [transação for transação in self.histórico.transaçoes if transação["tipo"] == Saque.__name__])
        ultrapassou_limite = valor > self.limite
        ultrapassou_saques = numero_saques >= self.limite_de_saques
        if ultrapassou_limite:
            print ("Limite ultrapassado!")
        elif ultrapassou_saques:
            print ("Não é possíve fazer mais saques!")
        else:
            return super().sacar(valor)
        return False
        def __str__(self):
            return f"""
            Agência: {self.agencia}
            Conta_Corrente: {self.numero}
            Titular: {self.cliente.nome}
            """

class histórico:
    def __init__(self):
        self._transacoes = []
    @property
    def transacoes(self):
        return self._transacoes
    def adicionar_transacao(self, transacao): 
        self._transacoes.append({
        "tipo": transacao._class________name_, 
        "valor": transacao.valor,
        }
        )
class Transação(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transação):
    def __init__(self, valor):
        self._valor
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.histórico.adicionar_transacao(self)

class Depósito(Transação):
        def __init__(self, valor):
            self._valor
        @property
        def valor(self):
            return self._valor
        def registrar(self, conta):
            sucesso_transacao = conta.sacar(self.valor)
            if sucesso_transacao:
                conta.histórico.adicionar_transacao(self)