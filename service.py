from app.repository import MessageRepository

class MessageService:
    """Business-logic layer."""
    def __init__(self):
        self.repository = MessageRepository()

    def get_messages(self):
        return self.repository.all()

    def add_message(self, name, message):
        name = str(name).strip()
        message = str(message).strip()
        if not name:
            raise ValueError("Please enter your name.")
        if not message:
            raise ValueError("Please enter a message.")
        if len(name) > 50:
            raise ValueError("Name must be 50 characters or fewer.")
        if len(message) > 300:
            raise ValueError("Message must be 300 characters or fewer.")
        return self.repository.create(name, message)
