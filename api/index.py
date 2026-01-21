from http.server import BaseHTTPRequestHandler
import json
from .crypto import encrypt, decrypt


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(
            b"Minecraft Crypto API is running. Use POST /api/index"
        )

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        body = self.rfile.read(length)
        data = json.loads(body)

        text = data.get("text", "")
        seed = int(data.get("seed", 0))
        mode = data.get("mode")

        if len(text) > 500:
            self.send_response(413)
            self.end_headers()
            self.wfile.write(b"Text terlalu panjang")
            return

        if mode == "encrypt":
            result = encrypt(text, seed)
        elif mode == "decrypt":
            result = decrypt(text, seed)
        else:
            result = "Invalid mode"

        response = {"result": result}

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
