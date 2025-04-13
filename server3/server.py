from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello I am SERVER3!')

if __name__ == "__main__":
    server_address = ('', 8899)  # Server1 works on port 8888
    httpd = HTTPServer(server_address, CustomHandler)
    print("Server3 works on port 8899...")
    httpd.serve_forever()

