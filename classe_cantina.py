#from Account import Account

class cantina():
    def __init__(self):
        self.Listadprodutos = []
        self.password = 'admin123'

    def NovoProduto(self, Produto, senha, qtdAdd, ValorCompra, DataCompra, Vencimento):
         #global Listadprodutos
         nProduto = {
             'nome':Produto, 
             'senha': senha, 
             'qtdAdd': qtdAdd, 
             'Valor da Compra':ValorCompra, 
             'Data da Compra':DataCompra, 
             'Vencimento': Vencimento
        }
         self.Listadprodutos.append(nProduto)
   
    def exibir(idProduto): #dados de um produto
        global Listadprodutos
        print('Id do Produto: ', idProduto)
        thisProductDict = Listadprodutos[idProduto]
        print('       Nome:', thisProductDict['nome'])
        print('       Quantidade: ', thisProductDict['qtdAdd'])
        print('       Valor da Compra:', thisProductDict['Valor da Compra'])
        print('       Data da Compra:', thisProductDict['Data da Compra'])
        print('       Vencimento:', thisProductDict['Vencimento'])
        print()

    def inventario(self, idProduto, senha): #inventário ou quantidade
        thisAccountDict = Listadprodutos[idProduto]
        if senha != thisAccountDict['senha']:
            print('Senha errada')
            return None
        return thisAccountDict['qtdAdd']

    def repositor(self, idProduto, qtdAdd, senha): #adcionar produto COM SENHA
        global Listadprodutos
        thisAccountDict = Listadprodutos[idProduto]
        if qtdAdd < 0:
            print('Você não pode adicionar produtos negativos')
            return None
        
        if senha != thisAccountDict['senha']:
            print('Senha incorreta')
            return None
    
        thisAccountDict['qtdAdd'] = thisAccountDict['qtdAdd'] + qtdAdd
        return thisAccountDict['qtdAdd']
    
    def compra(self, idProduto, qtdBuy): #reritada de produto sem senha
        global Listadprodutos
        thisAccountDict = Listadprodutos[idProduto]
        if qtdBuy < 0:
            print('Você não pode comprar uma quantidade negativa') #compra negativa
            return None
        
        if qtdBuy > thisAccountDict['qtdAdd']: #compra além da quantidade
            print('You cannot withdraw more than you have in your account')
            return None

        thisAccountDict['qtdAdd'] = thisAccountDict['qtdAdd'] - qtdBuy
        return thisAccountDict['qtdAdd'] #quantidade após a compra

    
