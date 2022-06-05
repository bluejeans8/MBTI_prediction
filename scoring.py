
import csv
import re
import pandas as pd
from konlpy.tag import Okt
from mbti_categories import *
from user import *


def parsing(line):
    i = 1
    name = ""
    while line[i] != ']':
        name += line[i]
        i += 1
    i += 1
    while line[i] != ']':
        i += 1
    message = line[i+1:]
    return name, message


def parse_and_tag(file_path):
    okt = Okt()
    data = dict()
    # 첫번째 참가자 이름
    p1_name = ""
    # 두번째 참가자 이름
    p2_name = ""
    # use regular expression
    kakao_msg_pattern = "오\S [0-9]{1,2}:[0-9]{1,2}"
    # 채팅을 한줄씩 읽기
    for line in file_path:
        if re.search(kakao_msg_pattern, line):
            cur_name, message = parsing(line)

            # 대화 참여자 이름을 추출 및 저장 과정
            if p1_name == "":
                p1_name = cur_name
            elif p2_name == "" and p1_name != cur_name:
                p2_name = cur_name
            elif p1_name != cur_name and p2_name != cur_name:
                continue

            # 각 대화 참여자 별로 채팅 내역을 tag 후 저장
            pos = okt.pos(message)
            if cur_name in data:
                data[cur_name] += pos
            else:
                data[cur_name] = pos
        else:
            continue
    # 결과를 DataFrame 형태로 리턴
    result = pd.DataFrame([data])
    print(result)
    result.columns = [p1_name, p2_name]
    return result


# 채팅 내역을 비교, 두 유저의 mbti_score 를 update
def score_mbti(p1_user, p1_chat, p2_user, p2_chat):

    for axis in Mbti:
        p1_count, p2_count = score_each_axis(p1_chat, p2_chat, axis)
        if p1_count == 0 and p2_count == 0:
            print("표본 오류:", p1_user, p2_user)
            exit(-1)
        else:
            ratio = p1_count / (p1_count + p2_count)
            p1_user.acc_score[axis] += ratio * 100
            p2_user.acc_score[axis] += (1 - ratio) * 100


# Mbti axis (E, N, F, J) 별로 해당 category 의 val 존재 counting
def score_each_axis(p1_chat, p2_chat, axis):
    p1_count, p2_count = 0, 0
    for val in morphemes[axis]:
        for tagged_word in p1_chat:
            if tagged_word == val:
                p1_count += 1
        for tagged_word in p2_chat:
            if tagged_word == val:
                p2_count += 1
    print("p1 유저", axis, "갯수:", p1_count)
    print("p2 유저", axis, "갯수:", p2_count)
    return p1_count, p2_count


