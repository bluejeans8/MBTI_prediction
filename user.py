from mbti_categories import *
import numpy as np
import matplotlib.pyplot as plt
# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc


class User:
    def __init__(self, name):
        self.name = name
        self.acc_score = {Mbti.E: 0, Mbti.N: 0, Mbti.F: 0, Mbti.J: 0}
        self.compare_count = 0

    # 각 mbti axis에 해당하는 점수를 반환
    def mbti_score(self):
        user_score = {key: (value / self.compare_count) for key, value in self.acc_score.items()}
        return user_score

    # 유저의 예상 mbti 문자열을 반환
    def get_user_mbti_string(self):
        mbti_string = ""
        mbti_score = self.mbti_score()
        for key in mbti_score:
            if mbti_score[key] > 50:
                mbti_string += mbti_axis[key][0]
            else:
                mbti_string += mbti_axis[key][1]
        mbti_string = self.name + "씨의 예상 MBTI는 " + mbti_string + "입니다."
        return mbti_string

    # 유저의 예상 mbti chart를 출력
    def display_chart(self):
        font_path = "C:/Windows/Fonts/NGULIM.TTF"
        font = font_manager.FontProperties(fname=font_path).get_name()
        rc('font', family=font)

        int_mbti_score = {key: int(value) for key, value in self.mbti_score().items()}

        results = {
            '외향 E / 내향 I': [int_mbti_score[Mbti.E], 100 - int_mbti_score[Mbti.E]],
            '직관 N / 감각 S': [int_mbti_score[Mbti.N], 100 - int_mbti_score[Mbti.N]],
            '감정 F / 사고 T': [int_mbti_score[Mbti.F], 100 - int_mbti_score[Mbti.F]],
            '판단 J / 인식 P': [int_mbti_score[Mbti.J], 100 - int_mbti_score[Mbti.J]],
        }

        category_names = ['Former %', 'Latter %']

        labels = list(results.keys())
        data = np.array(list(results.values()))
        data_cum = data.cumsum(axis=1)
        category_colors = plt.get_cmap('RdYlBu')(np.linspace(0.15, 0.85, data.shape[1]))

        fig, ax = plt.subplots(figsize=(9.2, 5))
        ax.invert_yaxis()
        ax.xaxis.set_visible(False)
        ax.set_xlim(0, np.sum(data, axis=1).max())
        ax.set_title('본인의 MBTI® 성격유형 결과 (Myers-Briggs Type Indicator®)')

        for i, (col_name, color) in enumerate(zip(category_names, category_colors)):
            widths = data[:, i]
            starts = data_cum[:, i] - widths
            rects = ax.barh(labels, widths, left=starts, height=0.5,
                            label=col_name, color=color)

            r, g, b, _ = color
            text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
            ax.bar_label(rects, label_type='center', color=text_color)
        ax.legend(ncol=len(category_names),
                  loc='upper right', fontsize='small')

        plt.figtext(0.5, 0.05, self.get_user_mbti_string(), ha="center", fontsize=12, color="white",
                    bbox={"boxstyle": "round", "facecolor": "purple", "alpha": 0.5, "pad": 0.5})

        return fig, ax
