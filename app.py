from flask import Flask, request
from flask import render_template
from calculadora_logica import app_calc

app = Flask(__name__)

def montar_tabela(data):
    tabela = {}
    for chave in data.keys():
        cont = 0
        for chave_valor in data[chave]:
            row = tabela.get(f"row_{cont}")
            if not row:
                tabela[f"row_{cont}"] = []
                tabela[f"row_{cont}"].append(chave_valor)
            else:
                tabela[f"row_{cont}"].append(chave_valor)
            cont += 1
    return tabela

@app.route("/")
def index():
    expressao = request.args.get("expressao", {})
    tabela = None
    error = None
    if expressao:
        try:
            expressao = app_calc(expressao)
            tabela = montar_tabela(expressao)
        except:
            error = True
    return render_template("index.html", tabela=tabela, expressao=expressao, error=error)


if __name__ == "__main__":
	app.run(debug=True)