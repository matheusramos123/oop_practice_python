# Classe que representa um produto em um sistema de estoque
class Produto():
    def __init__(self,nome,preco,quantidade):
        # Atributos principais do produto e uso de atributos privados
        self.nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
    # Método para comprar uma certa quantidade do produto
    def comprar_quant(self,n_produtos):
        # Verifica se há estoque suficiente
        if n_produtos <= self.__quantidade:
            # Reduz a quantidade em estoque    
            self.__quantidade -= n_produtos
            print(f'Nova quantidade: {self.__quantidade}')
        else:
            # Caso não haja produtos suficientes
            print('Produtos insuficiente para a quantidade que deseja!')
    
    # Método para repor produtos no estoque
    def repor(self,r_produtos): 
        # Impede reposições com valores inválidos
        if r_produtos <= 0:
            print('Valor invalido para repor!')
        else:
            # Aumenta a quantidade em estoque
            self.__quantidade += r_produtos
            print(f'Nova quantidade com reposição feita:  {self.__quantidade} Produtos!')
    # Método para calcular o valor total do estoque (preço × quantidade)
    def valor_estoque(self):
        return  self.__preco * self.__quantidade
    # Getter do atributo "preco"
    @property
    def preco(self):
        return self.__preco
    # Setter do atributo "preco"
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print('Não aceitamos valores negativos!')
    # Getter do atributo "quantidade"
    @property
    def quantidade(self):
        return self.__quantidade