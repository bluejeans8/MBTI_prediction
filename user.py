from mbti_categories import *


class User:
    def __init__(self, name):
        self.name = name
        self.acc_score = {Mbti.E: 0, Mbti.N: 0, Mbti.F: 0, Mbti.J: 0}
        self.compare_count = 0

    def mbti_score(self):
        e_score = self.acc_score[Mbti.E] / self.compare_count
        n_score = self.acc_score[Mbti.N] / self.compare_count
        f_score = self.acc_score[Mbti.F] / self.compare_count
        j_score = self.acc_score[Mbti.J] / self.compare_count

        return {Mbti.E: e_score, Mbti.N: n_score, Mbti.F: f_score, Mbti.J: j_score}
