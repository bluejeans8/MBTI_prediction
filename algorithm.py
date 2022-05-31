from konlpy.tag import Kkma
from konlpy.utils import pprint

kkma = Kkma()
try:
    f = open('kakao.txt', 'r', encoding='utf-8')
    s = f.readlines()
    for line in s:
        try:
            pos= kkma.pos(line)
            print(pos)
        except:
            continue
except:
    print("error!")
finally:
    f.close()