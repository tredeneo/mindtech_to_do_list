from flask import Flask, request, jsonify, Response
from typing import List
import tarefa
import sys

tarefas: List[tarefa.tarefa] = []

sys.path.append(".")

app = Flask(__name__)


@app.route("/tarefa", methods=["GET"])
def pegar_tarefa():
    json = request.get_json()
    for i in tarefas:
        if json["titulo"] == i.titulo:
            return jsonify(i)

    return Response((json["titulo"]), status=404, mimetype="application/json")


@app.route("/tarefas", methods=["GET"])
def pegar_tarefas():
    return jsonify(tarefas)


@app.route("/tarefa", methods=["DELETE"])
def excluir_tarefa():
    json = request.get_json()
    for i in range(len(tarefas)):
        if json["titulo"] == tarefas[i].titulo:
            return jsonify(tarefas.pop(i))

    return Response((json["titulo"]), status=404, mimetype="application/json")


@app.route("/concluir_tarefa", methods=["POST"])
def concluir_tarefa():
    json = request.get_json()
    for i in tarefas:
        if json["titulo"] == i.titulo:
            i.concluir()
            return jsonify(i)

    return Response((json["titulo"]), status=404, mimetype="application/json")


@app.route("/atualizar_tarefa", methods=["POST"])
def atualizar_tarefa():
    json = request.get_json()
    for i in tarefas:
        if json["titulo"] == i.titulo:
            i.atualizar(json)
            return jsonify(i)

    return Response((json["titulo"]), status=404, mimetype="application/json")


@app.route("/tarefa", methods=["POST"])
def cadastrar_tarefa():
    json = request.get_json()
    for i in tarefas:
        if json["titulo"] == i.titulo:
            return Response((json["titulo"]), status=409, mimetype="application/json")

    tarefa_atual = tarefa.tarefa(json)
    tarefas.append(tarefa_atual)
    return jsonify(tarefa_atual)


if __name__ == "__main__":
    app.run()
