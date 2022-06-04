from mbti_categories import *


class User:
    def __init__(self, name):
        self.name = name
        self.score = {Mbti.E: 0, Mbti.N: 0, Mbti.F: 0, Mbti.J: 0}

    def mbti_score(self):
        return self.score
