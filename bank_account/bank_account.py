# Classe Banco com atributos públicos e privados

class Banco():
    def __init__(self,nome,numero,saldo):
        self.nome = nome
        self.numero = numero
        self.__saldo = saldo

    # Método público para depositar valores, impedindo depósitos nulos ou negativos
    def depositar_valor(self,valor):
        if valor > 0:
            self.__saldo= self.__saldo + valor
            print(f'Depósito de {valor}, realizado com sucesso.')
        else:
            print('Não aceitamos valores nulos, nem negativos!')
    # Getter e setter para o saldo, garantindo valores positivos e mantendo o atributo privado protegido

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,saldo):
        if saldo < 0:
            print('Valor não elegível para os critérios de saldo!')
        else:
            self.__saldo = saldo
            print('Saldo atualizado! Saldo atual: ',self.__saldo)

    # Valores finais
    def mostrar_info(self):
        print('Nome:',self.nome,'número da conta:',self.numero,'Saldo:',self.saldo)

# Criando uma conta e realizando um depósito para testar os métodos
conta1 = Banco('Carlos', '1234', 1500)
conta1.depositar_valor(100)
conta1.mostrar_info()