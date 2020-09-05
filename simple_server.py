import http.server

class CGIRequestHandler(http.server.CGIHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path="index.html"
        elif self.path == "/page":
            self.path = "cgi-bin/page.py"
        return http.server.CGIHTTPRequestHandler.do_GET(self)
    
Handler = CGIRequestHandler
PORT = 8001

server = http.server.HTTPServer(("",PORT),Handler)
server.serve_forever()