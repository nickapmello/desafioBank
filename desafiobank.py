# Estruturas de dados para armazenar usuários e contas
usuarios = []
contas = []
numero_conta_atual = 1

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, *, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(nome, data_nascimento, cpf, endereco):
    global usuarios
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Usuário com este CPF já cadastrado.")
    else:
        usuario = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco
        }
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

def criar_conta(cpf):
    global contas, numero_conta_atual
    if any(conta['cpf'] == cpf for conta in contas):
        print("Este usuário já possui uma conta.")
    else:
        conta = {
            "agencia": "0001",
            "numero_conta": numero_conta_atual,
            "cpf": cpf
        }
        contas.append(conta)
        numero_conta_atual += 1
        print("Conta criada com sucesso!")

def listar_contas():
    if not contas:
        print("Não há contas registradas.")
    else:
        print("\nLista de Contas:")
        for conta in contas:
            print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, CPF do Titular: {conta['cpf']}")

# Programa principal - menu
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Usuário
[a] Criar Conta
[lc] Listar Contas
[q] Sair

=> """

saldo = 0
limite = 5000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 5

while True:
    opcao = input(menu)
    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == 's':
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
    elif opcao == 'e':
        mostrar_extrato(saldo, extrato)
    elif opcao == 'c':
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento: ")
        cpf = input("CPF: ")
        endereco = input("Endereço (logradouro, número - bairro - cidade/sigla estado): ")
        criar_usuario(nome, data_nascimento, cpf, endereco)
    elif opcao == 'a':
        cpf = input("CPF do usuário para a conta: ")
        criar_conta(cpf)
    elif opcao == 'lc':
        listar_contas()
    elif opcao == 'q':
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
