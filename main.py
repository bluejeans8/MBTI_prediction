from user_DB import UserDB
from user import *
from scoring import *
import os
import csv
import re
import pandas as pd

user_DB = UserDB()
dir_name = "kakaotalk_texts"

for filename in os.listdir(dir_name):
    with open(os.path.join(dir_name, filename), 'r', encoding='utf-8') as f:
        rdr = csv.reader(f)
        df = pd.DataFrame(rdr)[4:][0]
        result = parse_and_tag(df)
        p1_name, p2_name = result.columns
        p1_chat, p2_chat = result[p1_name].values.tolist()[0], result[p2_name].values.tolist()[0]

        p1_user = user_DB.find_user(p1_name)
        # p1_name 을 가진 user 가 user_DB에 존재 하지 않는 경우 새로 User 객체를 만들고 DB에 넣는다
        if p1_user == -1:
            p1_user = User(p1_name)
            user_DB.add_user(p1_user)
        p1_user.compare_count += 1

        p2_user = user_DB.find_user(p2_name)
        # p2_name 을 가진 user 가 user_DB에 존재 하지 않는 경우 새로 User 객체를 만들고 DB에 넣는다
        if p2_user == -1:
            p2_user = User(p2_name)
            user_DB.add_user(p2_user)
        p2_user.compare_count += 1

        print("p1_유저:", p1_user.name, "p2_유저:", p2_user.name)
        # 채팅 내역을 비교, 두 유저의 mbti_score 를 update
        score_mbti(p1_user, p1_chat, p2_user, p2_chat)
        print(p1_user.name, "[E, N, F, J] 점수:", p1_user.mbti_score(), "비교 횟수:", p1_user.compare_count)
        print(p2_user.name, "[E, N, F, J] 점수:", p2_user.mbti_score(), "비교 횟수:", p2_user.compare_count)

    f.close()

user_DB.print_all_users_mbti()
user_DB.display_main_user_chart()




