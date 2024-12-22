class User:
    def __init__(self, user_id, name, username, email):

        self.id = user_id
        self.name = name
        self.username = username
        self.email = email

    def __str__(self):
        return f'{self.id}. {self.name} - {self.username}, {self.email}'