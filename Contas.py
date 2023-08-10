from datetime import datetime
import pytz  # ajustes de fuso horário (timezone)
from random import randint

class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos cliente.

    Atributos:
        nome: nome do cliente
        cpf: cpf do cliente
        agencia: agencia responsável pela conta do cliente
        num_conta: número da conta corrente do cliente
        saldo: saldo disponível na conta do cliente
        limite: limite de cheque especial do cliente
        transacoes: histórico de transações do cliente
    """
    # posso fazer docstring nos métodos também
    # help(ContaCorrente)

    @staticmethod   # método estático da classe que não usa nada da classe, apenas informa a data e hora
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):  # os _ antes dos atributos: não é pra setar manualmente, e sim através das outras funções
        self.nome = nome                               # se fosse __ o atributo não ficaria visível nas funções, não teria como setar ou utilizar esse atributo, ele ficaria "privado"
        self.cpf = cpf
        self._saldo = 0
        self._limite = None # não quero passar o valor ainda
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = []  # cartoes não tem _ porque está sendo usado na classe CartaoCredito também

    def consultar_saldo(self):
        print(f'Seu saldo atual é de R${self._saldo:,.2f}')

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):  # o _ é apenas uma convenção para dizer que essa função não deve ser utilizado no programa, foi criado apenas para uso em uma outra função
        self._limite = -1000  # defini o limite, mas poderia ser uma conta mais complexa pra definir o limite
        return self._limite

    def sacar(self, valor):
        if self._saldo - valor < self._limite_conta():  # não coloca apenas <0, agora depende do limite da conta
            print('Você não tem saldo suficiente para sacar esse valor.')
            self.consultar_saldo()  # quando eu chamo uma função da classe dentro de outra função, tem que usar o self
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_cheque_especial(self):
        print(f'Seu limite de cheque especial é de R${self._limite_conta():,.2f}')

    def consultar_historico_transacoes(self):
        print('Histórico de Transações (valor, saldo, data e hora):')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod  # método estático da classe que não usa nada da classe, apenas informa a data e hora
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = None
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0,9), randint(0,9), randint(0,9))
        self.limite = 1000
        self._senha = '1234'  # senha está com o _ porque é um atributo que NÃO DEVE ser alterado manualmente ou por qualquer usuário, mas sim através do getter e setter
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)  # adiciono todos os atributos do cartão usando o self para aquela conta corrente

    # a diferença de usar apenas um _ para restringir o uso do atributo é que com o _ a pessoa apenas vai usar uma função com esse atributo para consultar, sem fazer alteração nos valores
    # enquanto com o getter e setter, a pessoa pode fazer alterações mas de uma forma controlada e verificada

    @property  # getter
    def senha(self):
        return self._senha

    @senha.setter  # setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova senha inválida")
