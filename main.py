from Contas import ContaCorrente, CartaoCredito
from Agencias import Agencia, AgenciaComum, AgenciaVirtual, AgenciaPremium


# programa
conta_ale = ContaCorrente("Alexandre", "111.222.333-45", 1234, 34062)  # primeira instância criada da classe ContaCorrente

cartao_ale = CartaoCredito('Alexandre', conta_ale)  # primeira instãncia criada da classe CartaoCredito

conta_ale.nome = "João"
print(conta_ale.nome)

cartao_ale.senha = '2345'
print(cartao_ale.senha)

print(conta_ale.__dict__)  # dicionário com os atributos e valores usados com a classe
print(cartao_ale.__dict__)


agencia1 = Agencia(22223333, 2000000000, 4568)  # primeira instância da classe Agencia

agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 22224444, 152000000)
agencia_virtual.verificar_caixa()

agencia_comum = AgenciaComum(22225555, 2550000000)  # primeira instância da classe AgenciaComum

agencia_premium = AgenciaPremium(22226666, 5550000000)  # primeira instância da classe AgenciaPremium

agencia_virtual.depositar_paypal(20000)
print(f'O saldo na agência virtual é de R${agencia_virtual.caixa:,.2f}')
print(f'O saldo na agência virtual é de R${agencia_virtual.caixa_paypal:,.2f}')

agencia_premium.adicionar_cliente('José', 15000000000, 10000)
print(agencia_premium.clientes)
agencia_premium.adicionar_cliente('José', 15000000000, 50000000)
print(agencia_premium.clientes)