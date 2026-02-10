utilizadores = []
id_utilizadores = 1


def criar_utilizadores():
    print("")
    global id_utilizadores
    nome = input("digite o seu nome: ")
    email = input("digite o seu E-mail: ")
    telefone = input("digite o seu contacto: ")

    utilizador = {
        "id": id_utilizadores,
        "nome": nome,
        "email": email,
        "telefone": telefone
    }

    utilizadores.append(utilizador)
    id_utilizadores += 1
    print("Utilizador adicionado com sucesso!")


def listar_utilizadores():
    if not utilizadores:
        print("Nenhum utilizador registado!")
        return
    for u in utilizadores:
        print(
            f"ID: {u['id']} | Nome: {u['nome']} | E-mail: {u['email']} | Nº de Telefone: {u['telefone']}")


def actualizar():
    print("")
    id_ut = int(input("Digite o ID do Funcionário: "))
    for u in utilizadores:
        if u['id'] == id_ut:
            u['nome'] = input("Digite o nome: ")
            u['email'] = input("Digite o E-mail: ")
            u['telefone'] = input("Digite o Nº de Telefone: ")
            print("Dados actualizados com sucesso!")
            return
    print("Utilizador não encontrado.")


def remover():
    id_ut = int(input("digite o ID do Funcionário: "))
    for u in utilizadores:
        if u['id'] == id_ut:
            utilizadores.remove(u)
            print("Utilizador removido com sucesso!")

    print("utilizador não encntrado!")


def menu():
    while True:
        print("")
        print("Selecione uma das Opções: ")
        print("1- Adicionar Funcionário")
        print("2- Alterar os dados de um Funcionário ")
        print("3- Listar os Funcionários")
        print("4- Remover um Funcionário")
        print("0- Sair")
        print("")

        op = int(input("Faça a sua escolha: "))

        if op == 1:
            criar_utilizadores()
            menu()
        elif op == 3:
            listar_utilizadores()
            menu()
        elif op == 2:
            actualizar()
            menu()
        elif op == 4:
            remover()
            menu()
        elif op == 0:
            print("Saindo...")
        break
    else:
        print("Opção Inválida!")


menu()
