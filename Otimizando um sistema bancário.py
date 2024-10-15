import textwrap

def menu():
    menu = '''\n
    ==========MENU==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Cadastrar usuário
    [c] Criar conta corrente
    [lc]Listar contas
    [x] Sair

    => '''
    return input(textwrap.dedent(menu))

def depositar (saldo, valor,extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\t R$ {valor:.2f}\n'
        print('\n Depósito realizado com sucesso!')
    else :
        print('\n Operação falhou! Valor informado é inválido!')

    return saldo,extrato



def sacar(*, saldo,valor,extrato,limite,numero_saque, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque >= limite_saques

    if excedeu_saldo:
        print('\n Operação falhou, saldo insuficiente!')

    elif excedeu_limite:
        print('\n Operação falhou, excede o limite')

    elif excedeu_saque:
        print('\n Operação falhou, número de saques excedido!')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\t R$ {valor:.2f}\n'
        numero_saque += 1
        print('\n Saque realizado com sucesso!')

    else:
        print('\n Operação falhou, valor inválido!')

    return saldo, extrato


def mostrar_extrato( saldo,/,*, extrato):
    print('==========EXTRATO==========')
    print('Não foram feitas movimentações.' if not extrato else extrato)
    print(f'\nSaldo:\t\t R$ {saldo:.2f}')
    print('===========================')

def cadastrar_usuario(usuarios):
    cpf= input('Informe o CPF(somente números): ')
    usuario = filtrar_usuario (cpf,usuarios)

    if usuario:
        print('\n CPF já existente!')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço completo (logradouro, número, bairro, cidade e estado): ')

    usuarios.append({'nome': nome, 'data_nascimento':data_nascimento, 'cpf': cpf, 'endereço': endereco})

    print('Usuário cadastrado com sucesso!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print('\n Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
        
    print('\n Usuário não encontrado!')

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta ['agencia']}
            C/c:\t\t{conta ['numero_conta']}
            Titular:\t{conta ['usuario']['nome']}
        '''
        print('=' * 100)
        print(textwrap.dedent (linha))

def main():

    LIMITE_SAQUES = 3
    AGENCIA ='0001'

    saldo= 0
    extrato= ""
    limite= 2000
    numero_saque= 0
    usuarios=[]
    contas=[]


    while True:

        opcao = menu()

        if opcao == 'd':
            valor = float(input('Digite o valor do depósito: '))

            saldo,extrato = depositar (saldo,valor,extrato)

        
        elif opcao == 's':
            valor = float(input('Digite o valor do saque: '))

            saldo,extrato = sacar (
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saque = numero_saque,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == 'e':
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == 'u':
            cadastrar_usuario(usuarios)

        elif opcao == 'c' :
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == 'lc':
            listar_contas(contas)
            
        elif opcao == 'x':
            break

        else:
            print('\n Operação inválida, por favor selecione a opção desejada!')

main()
