from flask import Flask #é a classe do Flask do módulo flasK
#a1 = Aluno() --> não precisa de "new"

app = Flask("My application")
#app é uma instância da classe Flask


#página home -/(padrão da home é o barra)
#decorateor (@)-> notação para a função home

# @app.route # toda vez que tiver essa rota,  vá para home

#página home
@app.route("/")
def home():
    return"<h1>Home page</h1>"

#página de contatos
@app.route("/contato")
def contatos():
    return"<h1>Contato</h1>"

#tais funções devem ser executadas quando foram requisitadas pelo servidor

#rota + Função
#rota:  Definição de um pacote url
#função: Função python com retorno(string,int,outros)