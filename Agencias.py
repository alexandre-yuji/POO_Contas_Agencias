from random import randint


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nível recomendado. Caixa atual é de R${self.caixa:,.2f}')
        else:
            print(f'O valor de caixa está ok. Caixa atual é de R${self.caixa:,.2f}')

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))  # é uma tupla
        else:
            print('Não é possível realizar empréstimo. Dinheiro não disponível em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):  # herança de Agencia

    def __init__(self, site, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=1000)   # faz com que eu continue tendo os atributos do init da classe pai além de adicionar novos atributos. se não usassse o super, esse init criado agora substituiria o init da classe pai nessa classe AgenciaVirtual
        self.site = site
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):  # método específico para a classe AgenciaVirtual
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):  # método específico para a classe AgenciaVirtual
        self.caixa_paypal -= valor
        self.caixa += valor


class AgenciaComum(Agencia):  # herança de Agencia

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):  # herança de Agencia

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):  # polimorfismo
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)  # estou utilizando o mesmo método da classe Agencia, porém com a condição que satisfaz a AgenciaPremium
        else:
            print('O cliente não tem o patrimônio mínimo necessário para entrar na agência premium.')


# if __name__ == '__main__':  # impede que um outro arquivo que use esse arquivo como importação rode esses programas abaixo
