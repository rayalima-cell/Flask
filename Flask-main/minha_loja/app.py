from flask import Flask, render_template

lista = [
    {"Id": 1, "nome": "Notebook", "preco": 3499.90, "Categoria": "Eletrônico", "Quantidade": 2},
    {"Id": 2, "nome": "Mouse", "preco": 89.90, "Categoria": "Eletrônico", "Quantidade": 5},
    {"Id": 3, "nome": "Teclado", "preco": 249.90, "Categotia": "Eletrõnico", "Quantidade": 8},
]


app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return "A Tec-Loja foi feita para ajudar novos usúarios da tecnologia."

@app.route("/produtos")
def produtos():
    return render_template("produto.html", produtos=lista)

@app.route("/produto/<int:id>")

def detalhe_produto(id):
    produto = None
    for p in lista:
        if p["id"] == id:
            produto = p
            break
    return render_template("detalhe.html", produto=produto, id=id)

@app.route("/categoria/<nome>")
def categoria(nome):
    return render_template("categoria.html", nome=nome)

if __name__ == "__main__":
    app.run(debug=True)