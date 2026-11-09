# Activity 3: Simple Client–Server Application

## Project overview
This project is a small message exchange application that runs on your own computer (`localhost`). A browser acts as the client. A Python HTTP server receives requests, validates data, and returns JSON responses.

## Requirements
- Python 3.8 or later
- A modern web browser
- No third-party Python packages are required

## How to run
1. Download and extract the project ZIP.
2. Open the extracted `client_server_activity3` folder in VS Code or another editor.
3. Open a terminal in that folder.
4. Run:

   ```bash
   python server.py
   ```

   On some Windows installations, use `py server.py`.
5. Open this address in your browser: **http://localhost:8000**
6. Confirm that the page says **Server is running**.
7. Enter your name and a message, then click **Send to server**.
8. Confirm that the success message appears and your message is displayed in the messages list.
9. Take screenshots of the running application and successful message exchange for your assessment.

Stop the server with `Ctrl + C` in the terminal.

## Layered architecture

```text
PRESENTATION LAYER
Browser UI: index.html + style.css + client.js
        |
        | HTTP GET /api/messages
        | HTTP POST /api/messages (JSON)
        v
APPLICATION / API LAYER
server.py (HTTP request handler and response)
        |
        v
BUSINESS LOGIC LAYER
app/service.py (validation and message rules)
        |
        v
DATA ACCESS LAYER
app/repository.py (stores and retrieves message records)
```

### Layer responsibilities
1. **Presentation layer:** Displays the form and messages. JavaScript uses `fetch()` to send HTTP requests and receive JSON responses.
2. **Application/API layer:** `server.py` listens on `127.0.0.1:8000`, handles GET and POST requests, and sends JSON responses.
3. **Business logic layer:** `MessageService` checks that the name and message are not empty and enforces length limits.
4. **Data access layer:** `MessageRepository` creates and retrieves message records. This demonstration stores records in memory, so they reset when the server restarts.

## Demonstration of communication
- `GET /api/health`: client checks whether the server is running.
- `GET /api/messages`: client requests existing messages; server returns a JSON list.
- `POST /api/messages`: client sends the name and message as JSON; server validates and stores them, then returns HTTP status **201 Created**.
- If required fields are missing, the server returns **400 Bad Request** with an error message.

## Assessment evidence checklist
Capture these screenshots after running the project:
- **Screenshot 1:** Browser showing `http://localhost:8000` and the “Server is running” status.
- **Screenshot 2:** A name and message entered in the form before submission.
- **Screenshot 3:** The success response and submitted message displayed in the messages list.
- **Screenshot 4 (optional):** Terminal showing the server running at `http://localhost:8000`.

## Short assessment conclusion
The application demonstrates the client-server model using HTTP communication on a localhost environment. The browser client sends GET and POST requests to the Python server. The server processes requests through separate API, business logic, and data access layers, then returns JSON responses to the client. Successful submission and retrieval of a message demonstrate communication between the system components.


