import http.server
import socketserver

class DoomServer(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Mandatory headers for Doom 3 multithreading
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

PORT = 8080
print(f"Doom 3 Server starting on port {PORT}...")
with socketserver.TCPServer(""][{PORT}], DoomServer) as httpd:
    httpd.serve_forever()
