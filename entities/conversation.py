class Conversation:
    def __init__(
        self, 
        initial_goal: str,
        title: str
        ):
        self.initial_goal = initial_goal
        self.title = title
        self.messages = []
        

class Message:
    def __init__(
        self, 
        message: str,
        role: str
        ):
        self.message = message
        self.role = role
