import json


class History:
    def __init__(self):
        self.history = []

    def add_user_message(self, message):
        self.add_message("user", message)

    def add_response_message(self, message):
        self.add_message("assistant", message)

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})

    def get_all_user_message(self):
        return [record['content'] for record in self.history if record['role'] == 'user']

    def get_chat_history(self):
        return self.history
