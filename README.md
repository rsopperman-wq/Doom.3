# Doom.3
Doom 3 WebAssembly Port (Codespaces Edition)
This repository contains a high-performance web port of Doom 3 using WebAssembly (WASM). Due to modern browser security requirements (SharedArrayBuffer), this game requires a specific server setup with security headers to run.

How to Play
Because this game requires Cross-Origin-Opener-Policy headers, you cannot simply open the HTML file. Follow these steps:

1. Launch the Codespace
Click the Code button in this repo.

Select the Codespaces tab and click Create codespace.

2. Download the Engine Files
The engine files are not tracked in this repo to save space. Run these commands in the terminal to fetch them:


curl -L -o d3wasm.js https://cdn.jsdelivr.net/gh/gabrielcuvillier/d3wasm@master/d3wasm.js
curl -L -o d3wasm.wasm https://cdn.jsdelivr.net/gh/gabrielcuvillier/d3wasm@master/d3wasm.wasm

3. Start the Secure Server
Run the included Python script to host the game with the necessary security headers:


python3 serv.py

4. Open the Game
Go to the Ports tab at the bottom of the screen.

Right-click the Visibility for Port 8080 and change it to Public.

Click the Globe Icon (Local Address) to launch the game.

Wait: The game will download approximately 400MB of asset data. Check the Network Tab (F12) to monitor progress.

Project Structure
index.html: The main game entry point with the WASM loader.

serv.py: A custom Python HTTP server that enables COOP and COEP headers.

d3wasm.js/wasm: The Doom 3 engine logic (downloaded via curl).

Controls
Click Canvas: Lock mouse and start playing.

ESC: Unlock mouse.

WASD: Move.

Mouse: Look/Shoot.

serv.py
Make sure this file is in your main folder so the "python3 serv.py" command works for other users:

Python
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
with socketserver.TCPServer(("", PORT), DoomServer) as httpd:
    httpd.serve_forever()
