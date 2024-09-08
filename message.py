class Message:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message


class Announcement(Message):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"Announcement: {self.message}"

    def __repr__(self):
        return f"Announcement: {self.message}"


class HelpRequest(Message):
    def __init__(self, message, room):
        super().__init__(message)
        self.room = room

    def __str__(self):
        return f"Help Request in Room {self.room}: {self.message}"

    def __repr__(self):
        return f"Help Request in Room {self.room}: {self.message}"
