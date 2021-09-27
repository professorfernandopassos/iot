from flask import Flask, Request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Olá, Pessoas!</h1>"

@app.route("/sobre")
def sobre():
    return "<h2>Sobre o nosso software: Nanananana.</h2>"

@app.route("/cliente/<cliente>")
def mostra_cliente(cliente):
    return f'<h1>{cliente}</h1>'

@app.route("/hash/<senha>")
def hash_da_senha(senha):
    def fazer_hash_da_senha(senha):
        # faz hash da senha e armazena na propria variavel senha
        return senha
    return '{ "hash": "%s" }' % senha

if __name__ == "__main__":
    app.run(debug=True)