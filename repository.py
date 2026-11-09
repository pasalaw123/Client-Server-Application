class MessageRepository:
    """Data-access layer. Stores messages in memory for this demo."""
    def __init__(self):
        self._messages = [
            {"id": 1, "name": "Demo User", "message": "Hello from the client!", "created_at": "Demo record"}
        ]
        self._next_id = 2

    def all(self):
        return list(self._messages)

    def create(self, name, message):
        record = {
            "id": self._next_id,
            "name": name,
            "message": message,
            "created_at": "Just now"
        }
        self._messages.append(record)
        self._next_id += 1
        return record
