class Estoque():
    def entrada(self, produto, quantidade):
        self.produto = produto
        self.quantidade = int(quantidade)
        

    def compra(self, valor_compra, vencimento, data_entrada):
        self.valor_compra = float(valor_compra)
        self.vencimento = int(vencimento)
        self.data_entrada = int(data_entrada)

    def venda(self, valor_venda, data_venda):
        self.valor_venda = float(valor_venda)
        self.data_venda = int(data_venda)
        