from user_DB import UserDB
from user import *
from scoring import *
import os

user_DB = UserDB()

for filename in os.listdir("kakaotalk_texts"):
    with open(os.path.join("kakaotalk_texts", filename), 'r', encoding='utf-8') as f:
        p1_name, p1_chat, p2_name, p2_chat = get_pos(f)

        p1_user = user_DB.find_user(p1_name)
        # p1_name 을 가진 user 가 user_DB에 존재 하지 않는 경우 새로 User 객체를 만들고 DB에 넣는다
        if p1_user == -1:
            p1_user = User(p1_name, [0, 0, 0, 0])
            user_DB.add_user(p1_user)

        p2_user = user_DB.find_user(p2_name)
        # p2_name 을 가진 user 가 user_DB에 존재 하지 않는 경우 새로 User 객체를 만들고 DB에 넣는다
        if p2_user == -1:
            p2_user = User(p2_name, [0, 0, 0, 0])
            user_DB.add_user(p2_user)

        score_mbti(p1_user, p1_chat, p2_user, p2_chat)

    f.close()


