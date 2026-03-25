from classe_cantina import cantina, admin

#NovoProduto = cantina()
cantina=admin()

print("a identificação do produto Bolinho é: ", len(cantina.Listadprodutos))
#NovoProduto("Bolinho", 'adm123', 10,  1, '01/01/2025', '01/01/2025')  #(Produto, ValorCompra, DataCompra, Vencimento):
cantina.NovoProduto("Bolinho", 'adm123', 10,  1, '01/01/2025', '01/01/2025')
print("a identificação do produto Salgadinho é: ", len(cantina.Listadprodutos))
cantina.NovoProduto("Salgadinho", 'adm123', 10, 2, '01/01/2025', '01/01/2026') #(Produto, ValorCompra, DataCompra, Vencimento):

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
        senha = input('Digite a senha: ')
        
        #Quantidade = inventario(userAccountNumber, userPassword)
        qtd = cantina.inventario(idProduto, senha)
        
        if qtd is not None:
            
            print('A quantidade de produtos é: ', qtd)

    elif action == 'd':
        print('Adicionar novos produtos:') #adicionar mais produtos já cadastrado
        idProduto= input('Por favor entre com o código do produto') #cod do produto (lugar na lista?)
        idProduto = int(idProduto)
        qtd = int(input('Por favor adicione a quantidade do produto que deseja adicionar')) #quantidade que foi colocada na bandeja
        senha = input('Por favor digite a senha') #senha do adm da cantina
        #temos que adicionar a data da compra e a data do vencimento


        novoestoque = cantina.repositor(idProduto, qtd, senha)
        if novoestoque is not None:
            print('Novo estoque: ', novoestoque) #a nova quantidade de produtos
        
    elif action == 'n':
        print('Cadastrar um novo produto: ') #um novo produto na bandeja
        produtoNovo = input('Qual é o produto? ') #qual o nome do produto 
        NovaQtd = int(input('Qual é a quantidade que você deseja adicionar? ')) #qual é a quantidade que foi depositada
        NovaSenha = input('Qual é a senha que deseja? ') #a senha tem que ser padrão
        usuarioCompra = float(input("Qual foi o valor da compra? "))
        if usuarioCompra < 0:
                print('Não digite um valor negativo, execute novamente')
                break
        usuarioData = input('Quando foi a compra? ')
        usuarioVencimnto = input("Quando é o vencimento do produto? ")

        #temos que adicionar a data da compra e a data do vencimento

        ProdutoUsuario = len(cantina.Listadprodutos)
        cantina.NovoProduto(produtoNovo, NovaSenha, NovaQtd, usuarioCompra, usuarioData, usuarioVencimnto)
        print('Seu novo produto é: ', ProdutoUsuario)

    elif action == 's':   #show all
        print('Todos os produtos:')
        nAccounts = len(cantina.Listadprodutos)
        for accountNumber in range(0, nAccounts):
            cantina.exibir(accountNumber)

    elif action == 'w':
        print('Compra:') #compra
        idProduto = int(input('Por favoe entre com o codigo do produto ')) #qual produto
        qtdCompra = int(input('Por favor, quantos produtos você deseja comprar? ')) #quantidade de compra
        '''userPassword = input('Please enter the password: ')'''
         #não precisa de senha
#criar uma variavel para a data da compra e com o valor... (criar uma carteira onde vamos saber o valor do caixa)

 
        NovaQtd = cantina.compra(idProduto, qtdCompra)
        if NovaQtd is not None:
            print('A quantidade disponivel neste momento é: ', NovaQtd)       #mova quantidade do produto

    elif action == 'q':
        break

print('Obrigado por usuar a Cantina da Faatec RC')
