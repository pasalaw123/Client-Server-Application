# Activity 3 Assignment: Design and Implementation of a Client–Server Application

## 1. Introduction
The purpose of this activity is to design and implement a simple client-server application in a localhost environment. The application developed is a Message Exchange System. It allows a user to enter a name and message through a web browser. The browser sends the information to a local Python server, which validates and stores it before returning a response.

## 2. System components
- **Client:** A web browser displaying the user interface.
- **Server:** A Python HTTP server listening on localhost port 8000.
- **API endpoints:** `/api/health`, `/api/messages` (GET), and `/api/messages` (POST).
- **Data repository:** An in-memory repository that stores submitted messages while the server is running.

## 3. Layered architecture
The system uses four layers:
1. Presentation layer – HTML, CSS and JavaScript provide the user interface.
2. Application/API layer – receives HTTP requests and sends HTTP responses.
3. Business logic layer – validates user input before it is stored.
4. Data access layer – stores and retrieves message records.

This separation makes the application easier to understand, test, maintain and extend.

## 4. Communication process
1. The user opens `http://localhost:8000` in a browser.
2. The client sends a GET request to `/api/health` to check the server.
3. The client sends a GET request to `/api/messages` to retrieve messages.
4. The user enters a name and message and clicks **Send to server**.
5. JavaScript sends the information to the server using an HTTP POST request with JSON data.
6. The server passes the data to the business logic layer for validation.
7. The repository stores the valid message.
8. The server returns a successful JSON response with HTTP status 201.
9. The client refreshes the message list and displays the submitted message.

## 5. Testing and expected results

| Test | Action | Expected result |
|---|---|---|
| Server health | Open the application | “Server is running” appears |
| Retrieve messages | Load or refresh the page | Existing messages are displayed |
| Send valid message | Enter a name and message | Success response; message appears |
| Empty name/message | Submit incomplete data | Validation error is displayed |
| Unknown API path | Request an unsupported endpoint | 404 response |

## 6. Conclusion
The project successfully demonstrates the client-server architecture in a localhost environment. The browser and Python server communicate through HTTP requests and JSON responses. The layered design separates presentation, API handling, business rules and data storage. The application can be extended by adding a database, user authentication and additional client features.

## 7. Evidence
Insert screenshots captured from your own running application:
- Figure 1: Application opened on localhost.
- Figure 2: Message entered by the client.
- Figure 3: Successful server response and message displayed.
- Figure 4: Python server running in the terminal (optional).
