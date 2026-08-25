from flask import Flask
#Cria a aplicação Flask

app = Flask(__name__)

#Define uma rota
@app.route('/')
def index():
    return "Olá, mundo! O Flask OK"

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
