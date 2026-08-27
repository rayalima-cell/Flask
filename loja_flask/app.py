from flask import Flask, render_template
#Cria a aplicação Flask

app = Flask(__name__)

#Define uma rota
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/produtos")
def produtos():
    lista = [
        {"nome": "Notebook", "preco": 3499.90},
        {"nome": "Mouse",    "preco": 89.90},
        {"nome": "Teclado",  "preco": 249.90}
    ]
    return render_template("produtos.html", produtos=lista)

@app.route("/sobre")
def sobre():
    return "Esta é a página sobre."

@app.route("/produto/<int:id>")

def produto(id):
    return f"Exibindo produto com id {id}"

@app.route("/categoria/<nome>")
def categoria(nome):
    return f"Produtos da categoria: {nome}"


#Inicia o servidor

if __name__ == "__main__":
    app.run(debug=True)
