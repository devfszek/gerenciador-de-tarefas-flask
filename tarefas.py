class Tarefa:
    def __init__(self, titulo, concluida=False):
        self.titulo = titulo
        self.concluida = concluida

    def concluir(self):
        self.concluida = True

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "concluida": self.concluida
        }
