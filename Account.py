# Account class
from datetime import datetime

class Produtos():
    def __init__(self, nome, quantidade, senha, dataCompra, vencimento):
        self.nome = nome
        self.quantidade = int(quantidade)
        self.senha = senha
        self.dataCompra = dataCompra
        self.vencimento = vencimento
   
    def adicionar(self, qtdAdd, senha):
        if senha != self.senha:
            print('Senha errada')
            return None

        if qtdAdd < 0:
            print('Você não pode adicionar quantidade negativa')
            return None

        self.quantidade = self.quantidade + qtdAdd
        self.dataCompra = datetime.now()
        return self.quantidade
        
    def compra(self, qtdCompra): #, password):
        #if password != self.password:
         #   print('Incorrect password for this account')
          #  return None

        if qtdCompra < 0:
            print('Você não pode comprar uma quantidade negativa')
            return None

        if qtdCompra > self.quantidade:
            print('Você não pode comprar além da quantidade')
            return None

        self.quantidade = self.quantidade - qtdCompra
        return self.quantidade

    def quantidade(self, senha):
        if self.senha != self.senha:
            print('Sorry, incorrect password')
            return None
        return self.quantidade

    # Added for debugging
    def catalogo(self):
        print('       Produto:', self.nome)
        print('       Quantidade:', self.quantidade)
        print('       Senha:', self.senha)
        print()
