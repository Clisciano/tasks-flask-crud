# arquivo principal da aplicação
# importando a biblioteca flask
from flask import Flask
# criando uma instância da classe Flask
# passando o nome do módulo como argumento
# __name__ é uma variável especial do python
# que retorna o nome do módulo atual
# quando executado diretamente, o valor é __main__
app = Flask(__name__)
# criando uma rota na raiz do site
@app.route('/')
# função que será executada quando acessar a rota
def hello_world():
    return 'Hello, World!'
# criando uma rota sobre a empresa
@app.route('/about')
# função que será executada quando acessar a rota about
def about():
    return 'Página sobre a empresa'


# se o módulo for executado diretamente pelo python modo desenvolvimento
if __name__ == '__main__':
    # executa o servidor web embutido
    app.run(debug=True)