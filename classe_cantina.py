#from Account import Account

class cantina():
    def __init__(self):
        self.Listadprodutos = []
    

    password = 'admin123'

    def NovoProduto(Produto, senha, qtdAdd, ValorCompra, DataCompra, Vencimento):
         global Listadprodutos
         NovoProduto = {'nome':Produto, 'senha': senha, 'qtdAdd': qtdAdd, 'Valor da Compra':ValorCompra, 'Data da Compra':DataCompra, 'Vencimento': Vencimento}
         Listadprodutos.append(NovoProduto)
   
    def exibir(idProduto): #dados de um produto
        global Listadprodutos
        print('Produto', idProduto)
        thisProductDict = Listadprodutos[idProduto]
        print('       Nome:', thisProductDict['nome'])
        print('       Quantidade: ', thisProductDict['qtdAdd'])
        print('       Valor da Compra:', thisProductDict['Valor da Compra'])
        print('       Data da Compra:', thisProductDict['Data da Compra'])
        print('       Vencimento:', thisProductDict['Vencimento'])
        print()

    def inventario(idProduto, senha): #inventário ou quantidade
        global Listadprodutos
        thisAccountDict = Listadprodutos[idProduto]
        if senha != thisAccountDict['senha']:
            print('Senha errada')
            return None
        return thisAccountDict['qtdAdd']

    def repositor(idProduto, qtdAdd, senha): #adcionar produto COM SENHA
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
    
    def compra(idProduto, qtdBuy): #reritada de produto sem senha
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

    
