class UserDB:

    Users = []

    # UserDB에 새로운 유저를 추가
    def add_user(self, user):
        self.Users.append(user)

    # name 을 가진 유저를 UserDB 에서 찾음
    def find_user(self, name):
        for user in self.Users:
            if user.name == name:
                return user
        return -1

