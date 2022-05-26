import menuADM
import operacoes
import this
this.opcao = -1
def menu():
    print('\n\nAdm Funcionários: Escolha uma das opções abaixo: \n\n' +
            '1. Cadastrar Funcionário\n'                        +
            '2. Consultar Funcionário\n'                        +
            '3. Atualizar Nome do Funcionário\n'                   +
            '4. Atualizar Celular do Funcionário\n'               +
            '5. Atualizar Salário do Funcionário\n'               +
            '6. Atualizar Senha do Funcionário\n'               +
            '7. Excluir Funcionário\n'               +
            '8. Voltar\n'                          +
            '0. Sair')
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            # Coletando a digitação do usuário
            print('Digite o Nome: ')
            nomeFunc = input()
            print('Digite o CPF: ')
            cpfFunc = input()
            if operacoes.cpf_validate(cpfFunc):
                print('CPF válido.')
            else:
                operacao()
            print('Digite o Celular: ')
            celularFunc = input()
            print('Digite o valor do Salário: ')
            salarioFunc = input()
            print('Digite a  Senha: ')
            senhaFunc = input()
            # utilizar o método cadastrar
            if nomeFunc + cpfFunc + celularFunc + salarioFunc + senhaFunc == "":
                print("Favor não deixe nenhum espaço em branco, Tente novamente!")
            else:operacoes.inserirFunc(nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc)
        elif this.opcao == 2:
            operacoes.selecionarFunc()
        elif this.opcao == 3:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigoFunc = input()
            print('Informe o novo Nome: ')
            nomeFunc = input()
            # Uso do método
            if codigoFunc + nomeFunc == "":
                print("Favor não deixe nenhum espaço em branco, Tente novamente!")
            else:operacoes.atualizarNomeFunc(codigoFunc, nomeFunc)
        elif this.opcao == 4:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigoFunc = input()
            print('Informe o novo Celular: ')
            celularFunc = input()
            # Uso do método
            if codigoFunc + celularFunc == "":
                print("Favor não deixe nenhum espaço em branco, Tente novamente!")
            else:operacoes.atualizarCelularFunc(codigoFunc, celularFunc)
        elif this.opcao == 5:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigoFunc = input()
            print('Informe o novo Salário: ')
            salarioFunc = input()
            # Uso do método
            if codigoFunc + salarioFunc == "":
                print("Favor não deixe nenhum espaço em branco, Tente novamente!")
            else:operacoes.atualizarSalario(codigoFunc, salarioFunc)
        elif this.opcao == 6:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigoFunc = input()
            print('Informe o novo Senha: ')
            senhaFunc = input()
            # Uso do método
            if codigoFunc + senhaFunc == "":
                print("Favor não deixe nenhum espaço em branco, Tente novamente!")
            else:operacoes.atualizarSenhaFunc(codigoFunc, senhaFunc)
        elif this.opcao == 7:
            print('Informe o código: ')
            codigoFunc = input()
            if codigoFunc == "":
                print("Favor não deixe nenhum espaço em branco, Tente novamente!")
            else:operacoes.excluirFunc(codigoFunc)
        elif this.opcao == 8:
            menuADM.operacao()
        elif this.opcao == 0:
            print('Obrigado!')