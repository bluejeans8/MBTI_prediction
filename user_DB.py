class UserDB:

    Users = []

    def add_user(self, user):
        self.Users.append(user)

    def find_user(self, name):
        for user in self.Users:
            if user.name == name:
                return user
        return -1

