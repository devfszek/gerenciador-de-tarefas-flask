from flask import Flask, render_template, request, redirect, url_for
from tarefas import Tarefa
from arquivo import carregar, salvar

app = Flask(__name__)

@app.route("/")
def index():
    tarefas = carregar()
    return render_template ("index.hmtl", tarefas=tarefas)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = request.form.get("titulo")

    if titulo:
        tarefas = carregar()
        tarefa = Tarefa(titulo)
        tarefas.append(tarefa.to_dict())
        salvar(tarefas)

    return redirect(url_for("index"))

@app.route("/concluir/<int:idx>")
def concluir(idx):
    tarefas = carregar()
    if 0 <= idx < len(tarefas):
        tarefas[idx]["concluida"] = True
        salvar(tarefas)
    return redirect(url_for("index"))

@app.route("/remover/<int:idx>")
def remover(idx):
    tarefas = carregar()
    if 0 <= idx < len(tarefas):
        tarefas.pop(idx)
        salvar(tarefas)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
