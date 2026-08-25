from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Bem-Vindos a Tec-Loja"

@app.route("/sobre")
def sobre():
    return "A Tec-Loja foi feita para ajudar novos usúarios da tecnologia."

@app.route("/produtos")

def produtos():
    print("=== PRODUTOS ===")
    print("1. Teclado 100% magnetico")
    print("2. Monitor LG UltraGear ")
    print("3. Mouse")

    produtos=["Teclado 100% magnetico", "Monitor LG UltraGear ", "Mouse"]
    return f"produtos = {produtos}"

@app.route("/produto/<int:id>")

def produto(id):
    return f"Exibindo id: {id}"

if __name__ == "__main__":
    app.run(debug=True)