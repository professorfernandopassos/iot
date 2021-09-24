from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = 'localhost'
PORT = 5000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>AULA HTTP</title></head>","utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Servidor HTTP de exemplo.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

webServer = HTTPServer((HOST,PORT), MyHandler)
print("Servidor iniciado em http://%s:%s" % (HOST, PORT))

webServer.serve_forever()