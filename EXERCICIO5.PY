    
class Conta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def sacar(self, valor):
        if valor <= 0:
            return "O valor do saque deve ser positivo."
        if valor > self.saldo:
            return "Saldo insuficiente."
        self.saldo -= valor
        return f"Saque de R${valor:.2f} realizado com sucesso."

    def depositar(self, valor):
        if valor <= 0:
            return "O valor do depósito deve ser positivo."
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso."

    def verificar_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"

class CaixaEletronico:
    def __init__(self):
        # Inicializa contas com saldo inicial
        self.conta_corrente = Conta(1000.00)
        self.conta_poupanca = Conta(500.00)

    def menu(self):
        while True:
            print("\n=== Caixa Eletrônico ===")
            print("1 - Saque")
            print("2 - Depósito")
            print("3 - Transferência")
            print("4 - Saldo")
            print("5 - Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.saque()
            elif escolha == '2':
                self.deposito()
            elif escolha == '3':
                self.transferencia()
            elif escolha == '4':
                self.saldo()
            elif escolha == '5':
                print("Saindo do caixa eletrônico.")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def saque(self):
        conta = self.selecionar_conta()
        if conta:
            valor = float(input("Digite o valor do saque: R$"))
            print(conta.sacar(valor))

    def deposito(self):
        conta = self.selecionar_conta()
        if conta:
            valor = float(input("Digite o valor do depósito: R$"))
            print(conta.depositar(valor))

    def transferencia(self):
        origem = self.selecionar_conta()
        if origem:
            destino = self.selecionar_conta(destino=True)
            if destino:
                valor = float(input("Digite o valor da transferência: R$"))
                saque_resultado = origem.sacar(valor)
                if "realizado com sucesso" in saque_resultado:
                    print(destino.depositar(valor))
                else:
                    print(saque_resultado)

    def saldo(self):
        print("\n=== Saldo das Contas ===")
        print("1 - Conta Corrente")
        print("2 - Conta Poupança")
        escolha = input("Escolha a conta para verificar o saldo: ")
        if escolha == '1':
            print(self.conta_corrente.verificar_saldo())
        elif escolha == '2':
            print(self.conta_poupanca.verificar_saldo())
        else:
            print("Opção inválida.")

    def selecionar_conta(self, destino=False):
        print("\nEscolha a conta:")
        print("1 - Conta Corrente")
        print("2 - Conta Poupança")
        escolha = input("Digite o número da conta: ")
        if escolha == '1':
            return self.conta_corrente if not destino else self.conta_poupanca
        elif escolha == '2':
            return self.conta_poupanca if not destino else self.conta_corrente
        else:
            print("Opção inválida.")
            return None

# Inicializa e executa o caixa eletrônico
caixa = CaixaEletronico()
caixa.menu() 