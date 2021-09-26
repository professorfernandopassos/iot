# import http.client

# http.client.HTTPConnection(host)

# FETCH

from http.client import HTTPConnection

conexao = HTTPConnection('localhost:5000')
conexao.request("GET", "/")
resposta = conexao.getresponse()
pagina = resposta.read()

print(pagina)
