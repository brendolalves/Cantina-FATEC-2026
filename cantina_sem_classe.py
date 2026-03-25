# Non-OOP Bank ------>>>>>>> temos que criar uma classe e separar em um outro programa a linha 63 em diante (encapsular as funcões das ações do usuário)
# Version 5
# Any number of accounts - with a list of dictionaries

Listadprodutos = []
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

    '''if password != thisAccountDict['password']: #sem senha
        print('Incorrect password for this account')
        return None'''
    
    thisAccountDict['qtdAdd'] = int(thisAccountDict['qtdAdd'])

    if qtdBuy > thisAccountDict['qtdAdd']: #compra além da quantidade
        print('Você não pode comprar além do disponivel')
        return None

    thisAccountDict['qtdAdd'] = thisAccountDict['qtdAdd'] - qtdBuy
    return thisAccountDict['qtdAdd'] #quantidade após a compra


############################################################################################


# Create two sample accounts
print("a identificação do produto Bolinho é:" , len(Listadprodutos))
NovoProduto("Bolinho", "adm123",  100, 1, '01/01/2025', '01/01/2026')  #(Produto, ValorCompra, DataCompra, Vencimento):

print("a identificação do produto Salgadinho é", len(Listadprodutos))
NovoProduto("Salgadinho", "adm123", 10, 2,  "01/01/2026", '01/01/2026') #(Produto, ValorCompra, DataCompra, Vencimento):

while True:
    print()
    print('Presione "b" para descobrir a quantidade de produtos') #administrador
    print('Presione "d" para adionar um produto já existente') #administrador
    print('Precione "n" para criar um novo produto') #administrador
    print('Precione "w" para fazer uma compra') #cliente
    print('Precione "s" para exibir o catálogo') #cliente e adm
    print('Precione "q" para sair')
    print()

    action = input('O que você deseja fazer? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()
    
    if action == 'b':
        print('Quantidade de produtos:')
        idProduto = input('Por favor digite o codigo do produto')
        idProduto = int(idProduto)
        senha = input('Por favor digite a senha: ')
        #Quantidade = inventario(userAccountNumber, userPassword)
        Quantidade = inventario(idProduto, senha)
        if Quantidade is not None:
            print('A quantidade de produtos é: ', Quantidade)

    elif action == 'd':
        print('Adicionar novos produtos:') #adicionar mais produtos já cadastrado
        idProduto= input('Por favor entre com o  código do produto ') #cod do produto (lugar na lista?)
        idProduto = int(idProduto)
        userDepositAmount = input('Por favor adicione a quantidade do produto que deseja adicionar ') #quantidade que foi colocada na bandeja
        userDepositAmount = int(userDepositAmount)
        senha = input('Por favor digite a senha: ') #senha do adm da cantina
        #temos que adicionar a data da compra e a data do vencimento


        novacontagem = repositor(idProduto, userDepositAmount, senha)
        if novacontagem is not None:
            print('A quantidade de produtos é: ', novacontagem) #a nova quantidade de produtos
        
    elif action == 'n':
        print('Cadastrar um novo produto: ') #um novo produto na bandeja
        produtoNovo = input('Qual é o produto? ') #qual o nome do produto 
        NovaQtd = input('Qual é a quantidade que você deseja adicionar? ') #qual é a quantidade que foi depositada
        NovaQtd = int(NovaQtd)
        NovaSenha = input('Qual é a senha que deseja? ') #a senha tem que ser padrão
        usuarioCompra = input("Qual foi o valor da compra?")
        usuarioCompra = int(usuarioCompra)
        usuarioData = input('Qual foi a data da compra?')
        usuarioVencimnto = input("Quando é o vencimento do produto? ")

        #temos que adicionar a data da compra e a data do vencimento

        ProdutoUsuario = len(Listadprodutos)
        NovoProduto(produtoNovo, NovaSenha, NovaQtd, usuarioCompra, usuarioData, usuarioVencimnto)
        print('Seu novo produto é: ', ProdutoUsuario)

    elif action == 's':   #show all
        print('Todos os produtos:')
        tdsProdutos = len(Listadprodutos)
        for id in range(0, tdsProdutos):
            exibir(id)

    elif action == 'q':
        break

    elif action == 'w':
        print('Compra:') #compra
        userAccountNumber = input('Por favor entre com o código do produto:  ') #qual produto
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input('Quantos produtos você quer comprar?: ') #quantidade de compra
        userWithdrawAmount = int(userWithdrawAmount)
       # userPassword = input('Please enter the password: ') #não precisa de senha
#criar uma variavel para a data da compra e com o valor... (criar uma carteira onde vamos saber o valor do caixa)

 
        novacontagem = compra(userAccountNumber, userWithdrawAmount)
        if novacontagem is not None:
            print('A contagem de produtos é: ', novacontagem)       #mova quantidade do produto

print('Done')
