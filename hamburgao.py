import this
import menuCliente
import conexao
import mysql.connector

this.opcao = 0

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def PrecoLanche():
    sql = "select * from lanche where nomeLanche = '{Hamburgão}'"
    con.execute(sql)

    for (nomeLanche, descricaoLanche, valorLanche, quantidadeLanche) in con:
        print(valorLanche)
    print('\n')

def Preco ():
    print('O preço do Hamburgão é: R$' + str(PrecoLanche()) + ',00.')

def QuantidadeLanche():
    sql = "select * from lanche where quantidadeLanche = '{Hamburgão}'"
    con.execute(sql)

    for (nomeLanche, descricaoLanche, valorLanche, quantidadeLanche) in con:
        print(quantidadeLanche)
    print('\n')

def Quantidade():
    print('A quantidade disponível desse lanche é: ' + str(QuantidadeLanche()) + '.')

def CalculoQuant():
    this.quantidade - QuantidadeLanche()

def Selecao (nomeLanche, quantidadeLanche):
    print('Digite a quantidade que deseja comprar: ')
    this.quantidade = int(input())
    while (this.quantidade < 0) or (this.quantidade > QuantidadeLanche()):
        if (this.quantidade < 0) or (this.quantidade > QuantidadeLanche()):
            print('Informe uma quantidade acessível à disponível, por favor!')
            this.quantidade = int(input())
    sql = "update lanche set quantidadeLanche = '{}' where nomeLanche = '{Hamburgão}'".format(nomeLanche,quantidadeLanche)
    con.execute(sql)
    db_connection.commit()

def Calculo():
    return this.quantidade * QuantidadeLanche()

def Compra ():
    Preco()
    Quantidade()
    Selecao()
    print('---------------- O valor total da compra é: '+ str(Calculo()) +',00. ----------------\n')
def Menu ():
    Compra()
    print('Deseja:'
          '\n1. Realizar Compra' +
          '\n2. Cancelar Compra')
    this.opcao = int(input())

def operacao():
        # Mostrar o menu em tela
        while this.opcao != 2:
            Menu()
            #realizar operações
            if this.opcao == 1:
                #operacao para 1.
                Compra()
                print('O código do PIX é 12345678912, acesse https://www.picpay.com/site para efetuar pagamento.')
            elif this.opcao == 2:
                #opereção para 2.
                menuCliente.operacao()
            else:
                print('Opção escolhida inválida! Tente novamente com as opções fornecidas.')