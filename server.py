from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json
from app.service import MessageService

ROOT = Path(__file__).parent
service = MessageService()

class ClientServerHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT / "static"), **kwargs)

    def send_json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/messages":
            self.send_json(200, {"success": True, "messages": service.get_messages()})
        elif self.path == "/api/health":
            self.send_json(200, {"success": True, "status": "Server is running"})
        else:
            super().do_GET()

    def do_POST(self):
        if self.path != "/api/messages":
            self.send_json(404, {"success": False, "error": "Endpoint not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            data = json.loads(self.rfile.read(length).decode("utf-8"))
            message = service.add_message(data.get("name", ""), data.get("message", ""))
            self.send_json(201, {"success": True, "message": message})
        except ValueError as exc:
            self.send_json(400, {"success": False, "error": str(exc)})
        except Exception:
            self.send_json(400, {"success": False, "error": "Invalid request data"})

if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8000), ClientServerHandler)
    print("Client-server app running at http://localhost:8000")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()
