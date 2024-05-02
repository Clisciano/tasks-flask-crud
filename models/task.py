# criar modelos para a aplicação
# criar um diretório chamado models
# criar um arquivo chamado task.py
# importar a classe Flask
# from flask import Flask
# criar uma instância da classe Flask

# criar classe Task
class Task:
    def __init__(self, id, title, description, completed=False) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
    # criar metodo de retorno de dicionário
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }  
      
