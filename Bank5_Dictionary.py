# Non-OOP Bank ------>>>>>>> temos que criar uma classe e separar em um outro programa a linha 63 em diante (encapsular as funcões das ações do usuário)
# Version 5
# Any number of accounts - with a list of dictionaries

Listadprodutos = []
password = 'admin123'

def NovoProduto(Produto, ValorCompra, DataCompra, Vencimento):
    global Listadprodutos
    NovoProduto = {'nome':Produto, 'Valor da Compra':ValorCompra, 'Data da Compra':DataCompra, 'Vencimento': Vencimento}
    Listadprodutos.append(NovoProduto)
   
def exibir(accountNumber): #dados de um produto
    global Listadprodutos
    print('Produto', accountNumber)
    thisProductDict = Listadprodutos[accountNumber]
    print('       Nome:', thisProductDict['nome'])
    print('       Valor da Compra:', thisProductDict['Valor da Compra'])
    print('       Data da Compra:', thisProductDict['Data da Compra'])
    print('       Vencimento:', thisProductDict['Vencimento'])
    print()

def inventario(accountNumber, password): #inventário ou quantidade
    global Listadprodutos
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None
    return thisAccountDict['balance']

def deposit(accountNumber, amountToDeposit, password): #adcionar produto COM SENHA
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None
        
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None
    
    thisAccountDict['balance'] = thisAccountDict['balance'] + amountToDeposit
    return thisAccountDict['balance']
    
def withdraw(accountNumber, amountToWithdraw, password): #reritada de produto sem senha
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount') #compra negativa
        return None

    if password != thisAccountDict['password']: #sem senha
        print('Incorrect password for this account')
        return None

    if amountToWithdraw > thisAccountDict['balance']: #compra além da quantidade
        print('You cannot withdraw more than you have in your account')
        return None

    thisAccountDict['balance'] = thisAccountDict['balance'] - amountToWithdraw
    return thisAccountDict['balance'] #quantidade após a compra

# Create two sample accounts
print("Joe's account is account number:", len(Listadprodutos))
NovoProduto("Joe", 100, 'soup', '01/01/2025')  #(Produto, ValorCompra, DataCompra, Vencimento):

print("Mary's account is account number:", len(Listadprodutos))
NovoProduto("Mary", 12345, 'nuts', '01/01/2026') #(Produto, ValorCompra, DataCompra, Vencimento):

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
        userAccountNumber = input('Por favor digite o codigo do produto')
        userAccountNumber = int(userAccountNumber)
        #userPassword = input('Please enter the password: ')
        #Quantidade = inventario(userAccountNumber, userPassword)
        Quantidade = inventario(userAccountNumber)
        if Quantidade is not None:
            print('A quantidade de produtos é: ', Quantidade)

    elif action == 'd':
        print('Deposit:') #adicionar mais produtos já cadastrado
        userAccountNumber= input('Please enter the account number: ') #cod do produto (lugar na lista?)
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit: ') #quantidade que foi colocada na bandeja
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ') #senha do adm da cantina
        #temos que adicionar a data da compra e a data do vencimento


        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance) #a nova quantidade de produtos
        
    elif action == 'n':
        print('New Account:') #um novo produto na bandeja
        userName = input('What is your name? ') #qual o nome do produto 
        userStartingAmount = input('What is the amount of your initial deposit? ') #qual é a quantidade que foi depositada
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What password would you like to use for this account? ') #a senha tem que ser padrão

        #temos que adicionar a data da compra e a data do vencimento

        userAccountNumber = len(Listadprodutos)
        NovoProduto(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)

    elif action == 's':   #show all
        print('Todos os produtos:')
        nAccounts = len(Listadprodutos)
        for accountNumber in range(0, nAccounts):
            exibir(accountNumber)

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:') #compra
        userAccountNumber = input('Please enter your account number: ') #qual produto
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input('Please enter the amount to withdraw: ') #quantidade de compra
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ') #não precisa de senha
#criar uma variavel para a data da compra e com o valor... (criar uma carteira onde vamos saber o valor do caixa)

 
        newBalance = withdraw(userAccountNumber, userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)       #mova quantidade do produto

print('Done')
