from flask import Flask , render_template, request
#é a classe do Flask do módulo flasK
#a1 = Aluno() --> não precisa de "new"
from validate_docbr import CPF, CNPJ

app = Flask("My application") #app é uma instância da classe Flask
cpf = CPF()
cnpj = CNPJ()

#página home -/(padrão da home é o barra)
#decorateor (@)-> notação para a função home

# @app.route # toda vez que tiver essa rota,  vá para home



lista_produtos =[
        {"nome":"Espresso","descricao": "That's that me espresso "},   
    ]

#------------------------------------------

@app.route("/")
def home(): 
    return render_template("home.html")


@app.route("/contatos")
def contatos(): 
    return render_template("contatos.html")

@app.route("/produtos")
def produtos():
 return render_template("produtos.html", newsongs = lista_produtos)

#------------------------------------------

@app.route("/gerar-cpf")
def cpfgerar(): 
    cpfuser = cpf.generate(True)
    return render_template("cpf.html", cpf = cpfuser)


@app.route("/gerar-cnpj")
def CNPJ():
     cnpjuser = cnpj.generate(True) 
     return  render_template("cnpj.html", cnpj = cnpjuser)

#------------------------------------------
@app.route("/termos-de-uso")
def termosdeuso(): 
    return render_template("termosdeuso.html")

@app.route("/politica-privacidade")
def politicapriv(): 
    return render_template("politicadepriv.html")

@app.route("/como-utilizar")
def comoutilizar(): 
    return render_template("comoutilizar.html")

@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

@app.route("/produtos", methods = ['POST'])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    produto = {"nome": nome, "descricao": descricao}
    lista_produtos.append(produto)
    return render_template ("produtos.html", newsongs = lista_produtos)
app.run()

#tais funções devem ser executadas quando foram requisitadas pelo servidor

#rota + Função
#rota:  Definição de um pacote url
#função: Função python com retorno(string,int,outros)
#gerar-cpf 
#servicos


#https://color.adobe.com/pt/create/color-wheel