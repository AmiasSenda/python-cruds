import json
import os


arquivo = "utilizadores.json"


if os.path.exists(arquivo):
    print("")
    with open(arquivo, "r", encoding="utf-8") as f:
        utilizadores = json.load(f)
else:
    utilizadores = []
    id_utilizadores = 1


def salvar():
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(utilizadores, f, indent=4, ensure_ascii=False)


def criar_utilizadores():
    print("")
    id_utilizadores = max([u["id"] for u in utilizadores], default=0) + 1
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
            salvar()
    print("Utilizador não encontrado.")


def remover():
    id_ut = int(input("digite o ID do Funcionário: "))
    for u in utilizadores:
        if u['id'] == id_ut:
            utilizadores.remove(u)
            print("Utilizador removido com sucesso!")
            salvar()

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
