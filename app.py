# arquivo principal da aplicação
# importando a biblioteca flask
# criando uma instância da classe Flask
# passando o nome do módulo como argumento
# __name__ é uma variável especial do python
# que retorna o nome do módulo atual
# quando executado diretamente, o valor é __main__
from flask import Flask, request, jsonify
# importar o módulo task
from models.task import Task

app = Flask(__name__)
# criar uma variavel para armazenar a lista de tarefas
tasks = []
task_id_control = 1
# criar rota para adicionar tarefas
@app.route('/tasks', methods=['POST'])
def create_task():
   # criar variavel global para controlar o id da tarefa
   global task_id_control
    # recuperar dados vindo da requisição
   data = request.get_json()
    # criar uma nova tarefa
   new_task = Task(
    id=task_id_control,   
    title=data.get('title'), 
    description=data.get('description'), 
    completed=data.get('completed')
   )  
    # incrementar o id da tarefa
   task_id_control += 1 
    # adicionar a nova tarefa na lista de tarefas
   tasks.append(new_task)
   print('tasks:', tasks)
   return jsonify({'message': 'Task created successfully!'}), 200

# se o módulo for executado diretamente pelo python modo desenvolvimento
if __name__ == '__main__':
    # executa o servidor web embutido
    app.run(debug=True)