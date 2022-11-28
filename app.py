from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    # metodo_escolhido = request.args.get("metodo", None)
    # numeros = []
    # if metodo_escolhido:
    #     numeros = gerar_numero(metodo_escolhido)
    # return render_template("index.html", numeros=numeros, numeros_sorteados=pegar_todos_os_numeros_sorteados())
    return render_template("index.html")


if __name__ == "__main__":
	app.run(debug=True)