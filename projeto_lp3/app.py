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

#página home
@app.route("/")
def termosdeuso(): 
    return render_template("termosdeuso.html")

#página de contatos
@app.route("/contatoss")
def contatoss():
    return render_template("contato.html")

lista_produtos =[
        {"nome":"Espresso","descricao": "That's that me espresso "},   
    ]
@app.route("/produtos")
def prod():
 
    return render_template("produtos.html", newsongs = lista_produtos)


@app.route("/home")
def home2(): 
    return render_template("home2.html")

#------------------------------------------
@app.route("/gerar-cpf")
def cpfgerar(): 
    cpfuser = cpf.generate(True)
    return render_template("cpf.html", cpf = cpfuser)

@app.route("/gerar-cnpj")
def CNPJ():
     cnpjuser = cnpj.generate(True) 
     return  render_template("cnpj.html", cnpj = cnpjuser)
@app.route("/como-utilizar")
def comoutilizar(): 
    return render_template("comoutilizar.html")

@app.route("/politica-privacidade")
def politicapriv(): 
    return render_template("politicadepriv.html")

@app.route("/contatos")
def contatos(): 
    return render_template("contatos2.html")

@app.route("/produto")
def produtos(): 
    return render_template("produtos.html")

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