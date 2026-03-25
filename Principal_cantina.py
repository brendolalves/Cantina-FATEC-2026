from classe_cantina import cantina

#NovoProduto = cantina()
cantina=cantina()

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
        senha = input('Please enter the password: ')
        
        #Quantidade = inventario(userAccountNumber, userPassword)
        Quantidade = cantina.inventario(idProduto, senha)
        
        if Quantidade is not None:
            
            print('A quantidade de produtos é: ', Quantidade)

    elif action == 'd':
        print('Adicionar novos produtos:') #adicionar mais produtos já cadastrado
        idProduto= input('Por favor entre com o código do produto') #cod do produto (lugar na lista?)
        idProduto = int(idProduto)
        userDepositAmount = input('Por favor adicione a quantidade do produto que deseja adicionar') #quantidade que foi colocada na bandeja
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Por favor digite a senha') #senha do adm da cantina
        #temos que adicionar a data da compra e a data do vencimento


        newBalance = cantina.repositor(idProduto, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance) #a nova quantidade de produtos
        
    elif action == 'n':
        print('Cadastrar um novo produto:') #um novo produto na bandeja
        userName = input('Qual é o produto? ') #qual o nome do produto 
        userStartingAmount = input('Qual é a quantidade que você deseja adicionar? ') #qual é a quantidade que foi depositada
        userStartingAmount = int(userStartingAmount)
        userPassword = input('Qual e a senha que deseja? ') #a senha tem que ser padrão

        #temos que adicionar a data da compra e a data do vencimento

        userAccountNumber = len(cantina.Listadprodutos)
        cantina.NovoProduto(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)

    elif action == 's':   #show all
        print('Todos os produtos:')
        nAccounts = len(cantina.Listadprodutos)
        for accountNumber in range(0, nAccounts):
            cantina.exibir(accountNumber)

    elif action == 'q':
        break

    elif action == 'w':
        print('Compra:') #compra
        userAccountNumber = input('Por favoe entre com o codigo do produto ') #qual produto
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input('Por favor, quantos produtos você deseja comprar? ') #quantidade de compra
        userWithdrawAmount = int(userWithdrawAmount)
        '''userPassword = input('Please enter the password: ')'''
         #não precisa de senha
#criar uma variavel para a data da compra e com o valor... (criar uma carteira onde vamos saber o valor do caixa)

 
        newBalance = cantina.compra(userAccountNumber, userWithdrawAmount)
        if newBalance is not None:
            print('Your new balance is:', newBalance)       #mova quantidade do produto

print('Done')
