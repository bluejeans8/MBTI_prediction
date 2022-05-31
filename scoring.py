from konlpy.tag import Okt
from mbti_categories import *


def get_pos(f):
    okt = Okt()
    # 첫번째 참가자 대화 내용 및 이름
    p1_name = ""
    p1_chat = []
    # 두번째 참가자 대화 내용 및 이름
    p2_name = ""
    p2_chat = []

    s = f.readlines()
    # 채팅을 한줄씩 읽기
    for line in s:
        try:
            if line[:2] != "20":
                continue
            comma = line.find(",")
            if comma == -1:
                continue
            else:
                comma += 1
                name_and_chat = line[comma:]
                colon = name_and_chat.find(":")

                cur_name = name_and_chat[:colon-1]
                cur_chat = name_and_chat[colon+1:]

                # 대화 참여자 이름을 추출 및 저장 과정
                if p1_name == "":
                    p1_name = cur_name
                elif p2_name == "" and p1_name != cur_name:
                    p2_name = cur_name

                # 각 대화 참여자 별로 채팅 내역을 저장
                pos = okt.pos(cur_chat)
                if cur_name == p1_name:
                    p1_chat += pos
                elif cur_name == p2_name:
                    p2_chat += pos
        except:
            continue

    return p1_name, p1_chat, p2_name, p2_chat


def score_mbti(p1_user, p1_chat, p2_user, p2_chat):
    for axis in Mbti:
        p1_score, p2_score = score_each_axis(p1_chat, p2_chat, axis)
        if p1_score > p2_score:
            p1_user.score[axis] += 1
            p2_user.score[axis] -= 1
        elif p1_score < p2_score:
            p1_user.score[axis] -= 1
            p2_user.score[axis] += 1


def score_each_axis(p1_chat, p2_chat, axis):
    p1_score, p2_score = 0, 0
    for val in mbti[axis]:
        for tagged_word in p1_chat:
            if tagged_word == val:
                p1_score += 1
        for tagged_word in p2_chat:
            if tagged_word == val:
                p2_score += 1
    return p1_score, p2_score


