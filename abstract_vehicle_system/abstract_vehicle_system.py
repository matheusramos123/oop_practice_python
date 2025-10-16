# Importa o módulo abc (Abstract Base Class) para criar classes e métodos abstratos
import abc
# Classe base abstrata que representa um veículo genérico
class Veiculo(abc.ABC):
    def __init__(self,marca,modelo,ligado = False):
        self.marca  = marca
        self.modelo = modelo
        # Indica se o veículo está ligado ou não (por padrão, está desligado)
        self.ligado= ligado 
    # Método abstrato que deve ser implementado nas subclasses
    @abc.abstractmethod
    def ligar(self):
        pass
    # Outro método abstrato obrigatório para todas as subclasses
    @abc.abstractmethod
    def desligar(self):
        pass
# Classe que representa um carro, herdando de Veiculo
class Carro(Veiculo):
    def __init__(self,marca,modelo,ligado = False):
        super().__init__(marca, modelo, ligado)
    # Implementação concreta do método abstrato "ligar"
    def ligar(self):
        # Verifica se o carro está desligado
        if not self.ligado:
            self.ligado =  True
            print('Carro Ligado!')
        # Caso já esteja ligado, exibe uma mensagem informando
        else:
            print(f'O carro {self.marca} {self.modelo}, ja esta ligado!')
    # Implementação concreta do método abstrato "desligar"
    def desligar(self):
        # Verifica se o carro está ligado
        if self.ligado:
            self.ligado = False
            print(f'O carro  {self.marca} {self.modelo}, foi desligado!')
        else:
            print(f'O carro {self.marca} {self.modelo} já está desligado!')
# Classe que representa uma moto, também herdando de Veiculo
class Moto(Veiculo):
    def __init__(self,marca,modelo,ligado = False):
        # Chama o construtor da classe base (Veiculo)
        super().__init__(marca,modelo,ligado)
    # Implementação do método "ligar" específica para motos
    def ligar(self):
        if not self.ligado:
            self.ligado =  True
            print('Moto Ligada!')
        else:
            print(f'A Moto {self.marca} {self.modelo}, ja esta ligada!')
    # Implementação do método "desligar" específica para motos
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f'A moto  {self.marca} {self.modelo}, foi desligada!')
        else:
            print(f'A moto {self.marca} {self.modelo} já está desligada!')

