from mbti_categories import *


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

    def print_users_mbti(self):
        for user in self.Users:
            mbti_string = ""
            mbti_score = user.mbti_score()
            for key in mbti_score:
                if mbti_score[key] > 0:
                    mbti_string += mbti_axis[key][0]
                else:
                    mbti_string += mbti_axis[key][1]
            print(user.name, "MBTI는:", mbti_string)

