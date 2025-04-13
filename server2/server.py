from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello I am SERVER5!')

if __name__ == "__main__":
    server_address = ('', 8989)  # Server5 works on port 8989
    httpd = HTTPServer(server_address, CustomHandler)
    print("Server5 works on port 8989...")
    httpd.serve_forever()
