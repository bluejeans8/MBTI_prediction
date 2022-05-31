from mbti_categories import *


class User:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def mbti_score(self):
        e_score = self.score[Mbti.E]
        n_score = self.score[Mbti.N]
        f_score = self.score[Mbti.F]
        j_score = self.score[Mbti.J]
        return e_score, n_score, f_score, j_score
