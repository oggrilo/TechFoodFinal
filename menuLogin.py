import operacoes
import this
import conexao
this.opcao = -1

def menu():
    print('\n\nEscolha uma das opções abaixo: \n\n' +
            '1. Cadastrar Cliente\n' +
            '2. Login Cliente\n' +
            '3. Login Adiministrador\n' +
            '0. Sair')
    this.opcao = int(input())

def escolhas():
    while(this.opcao !=0 ):
        menu()
        if this.opcao == 1:
                # Coletando a digitação do usuário
                print('Digite seu nome: ')
                nomeCliente = input()
                print('Digite seu cpf: ')
                cpfCliente = input()
                if operacoes.cpf_validate(cpfCliente):
                    print('CPF válido.')
                else:
                    escolhas()
                print('Digite seu celular: ')
                celularCliente = input()
                print('Digite sua senha: ')
                senhaCliente = input()
                if nomeCliente + cpfCliente + celularCliente + senhaCliente == "":#validar para não permitir dados em branco
                    print("Favor não deixe nenhum espaço em branco, Tente novamente!")
                else:operacoes.inserirCliente(nomeCliente, cpfCliente, celularCliente, senhaCliente)
                # utilizar o método cadastrar
        elif this.opcao == 2:
            print("Digite seu CPF: ")
            cpfCliente= input()
            if operacoes.cpf_validate(cpfCliente):
                print('CPF válido.')
            else:
                escolhas()
            print("Digite sua senha: ")
            senhaCliente = input()
            if cpfCliente + senhaCliente == "":#validar para não permitir dados em branco
                print("Favor não deixe nenhum espaço em branco, Tente novamente!")
            else:operacoes.loginCliente(cpfCliente, senhaCliente)
        elif this.opcao == 3:
            print("Digite seu CPF: ")
            cpfFunc = input()
            if operacoes.cpf_validate(cpfFunc):
                print('CPF válido.')
            else:
                escolhas()
            print("Digite sua senha: ")
            senhaFunc = input()
            if cpfFunc + senhaFunc == "":#validar para não permitir dados em branco
                print("Favor não deixe nenhum espaço em branco, Tente novamente!")
            else:operacoes.loginFunc(cpfFunc, senhaFunc)
        else:
             print("Obrigado e até a proxima!")



