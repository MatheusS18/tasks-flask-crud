class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome  = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_info (self):
        print(f"Os dados do produto são esses: {self.nome}, {self.preco}, {self.quantidade} ")

    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"O novo preço do produto {self.nome} é R$ {self.preco}")

    def adicionar_estoque(self, qtd):
        estoque_antigo = self.quantidade
        self.quantidade += qtd
        print(f"O estoque foi atualizado de {estoque_antigo} para {self.quantidade}")

    def remover_estoque(self, qtd):
        if qtd <= self.quantidade:
            estoque_antigo = self.quantidade
            self.quantidade -= qtd
            print(f"O estoque foi atualizado de {estoque_antigo} para {self.quantidade}")
        else:
            print(f"Não é possível remover {qtd} unidades — estoque insuficiente ({self.quantidade})")


produto1 = Produto("Mouse", 150.0, 10)

produto1.exibir_info()

produto1.adicionar_estoque(5)
produto1.remover_estoque(3)
produto1.remover_estoque(20)  # Testando remover mais do que tem

produto1.atualizar_preco(120.0)
produto1.exibir_info()