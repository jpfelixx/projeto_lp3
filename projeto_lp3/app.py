from flask import Flask #é a classe do Flask do módulo flasK
#a1 = Aluno() --> não precisa de "new"
from validate_docbr import CPF, CNPJ

app = Flask("My application") #app é uma instância da classe Flask
cpf = CPF()
cnpj = CNPJ()

#página home -/(padrão da home é o barra)
#decorateor (@)-> notação para a função home

# @app.route # toda vez que tiver essa rota,  vá para home

#página home
@app.route("/")
def home(): 
    return"<h1> Home page</h1>"

#página de contatos
@app.route("/contato")
def contatos():
    return"<h1>Contato</h1>"


@app.route("/servicos")
def servicos():
    return"<h1>Nossos servicos</h1>"

@app.route("/gerar-cpf")
def cpfgerar(): 
    cpfuser = cpf.generate(True)
    return cpfuser

@app.route("/gerar-cnpj")
def CNPJ(): 
    return  f"<h1>Gerar cpf </h1><p>CPF: {cnpj.generate(True)}"     #"<h1>Gerador de cpf: </h1> <br> <div> O seu cnpj é:" + cnpj.generate(True)+ " </div>"

app.run()

#tais funções devem ser executadas quando foram requisitadas pelo servidor

#rota + Função
#rota:  Definição de um pacote url
#função: Função python com retorno(string,int,outros)

#gerar-cpf 
#servicos