from dataclasses import dataclass
import datetime


@dataclass
class tarefa:
    titulo: str
    descricao: str
    data_criacao: datetime.datetime
    data_conclusao: datetime.datetime
    finalizada: bool

    def __init__(self, json):
        self.titulo = json["titulo"]
        self.descricao = json["descricao"]
        self.data_conclusao = None
        self.data_criacao = datetime.date.today()
        self.finalizada = False

    def concluir(self):
        self.finalizada = True
        self.data_conclusao = datetime.date.today()

    def atualizar(self, json):
        self.titulo = json["novo_titulo"]
        self.descricao = json["nova_descricao"]
