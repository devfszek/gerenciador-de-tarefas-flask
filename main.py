from tarefas import Tarefa
from arquivo import carregar, salvar

tarefas = carregar()

def menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("0 - Sair")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return False

    for i, t in enumerate(tarefas):
        status = "✔" if t["concluida"] else "✖"
        print(f"{i} - {t['titulo']} [{status}]")
    return True

while True:
    menu()
    opcao = input("Escolha: ").strip()

    if opcao == "1":
        titulo = input("Título da tarefa: ").strip()
        if titulo == "":
            print("O título não pode ser vazio.")
            continue

        tarefa = Tarefa(titulo)
        tarefas.append(tarefa.to_dict())
        salvar(tarefas)
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        if not listar_tarefas():
            continue

        try:
            idx = int(input("Número da tarefa: "))
            tarefas[idx]["concluida"] = True
            salvar(tarefas)
            print("Tarefa concluída!")
        except (ValueError, IndexError):
            print("Número inválido.")

    elif opcao == "4":
        if not listar_tarefas():
            continue

        try:
            idx = int(input("Número da tarefa: "))
            tarefas.pop(idx)
            salvar(tarefas)
            print("Tarefa removida!")
        except (ValueError, IndexError):
            print("Número inválido.")

    elif opcao == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
