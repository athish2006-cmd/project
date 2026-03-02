from http.server import HTTPServer, SimpleHTTPRequestHandler
HOST = "localhost"
PORT = 8000
if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    server.serve_forever()