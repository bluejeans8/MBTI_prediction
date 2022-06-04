from enum import IntEnum


# Mbti axis index
class Mbti(IntEnum):
    E = 0
    N = 1
    F = 2
    J = 3


# mbti axis for print string
mbti_axis = {Mbti.E: ("E", "I"), Mbti.N: ("N", "S"), Mbti.F: ("F", "T"), Mbti.J: ("J", "P")}


# Morphological units
morphemes = {Mbti.E: [('랑', 'Josa'), ('이랑', 'Josa'), ('자', 'Josa')], Mbti.N: [('면', 'Josa'), ('텐데', 'Eomi'), ('을까', 'Eomi'), ('이었음', 'Eomi'), ('였음', 'Eomi'), ('면은', 'Eomi'), ('을거야', 'Eomi'), ('인가', 'Josa'), ('엄청', 'Adverb'), ('그냥', 'Noun'), ('걍', 'Adverb')], Mbti.F: [('아', 'Exclamation'), ('엉', 'Exclamation'), ('야', 'Exclamation'), ('하', 'Exclamation'), ('엥', 'Exclamation'), ('휴', 'Exclamation'), ('우웅', 'Exclamation'), ('오호', 'Exclamation'), ('아이고', 'Exclamation'), ('오오', 'Exclamation'), ('우와', 'Exclamation'), ('아오', 'Exclamation'), ('앙', 'Exclamation'), ('어휴', 'Exclamation'), ('헿', 'Exclamation'), ('으으', 'Exclamation'), ('플', 'Exclamation'), ('힣', 'Exclamation'), ('하아', 'Exclamation'), ('아이구', 'Exclamation'), ('크크', 'Exclamation'), ('아아', 'Exclamation'), ('뭐', 'Exclamation'), ('우아', 'Exclamation'), ('후후', 'Exclamation'), ('핳', 'Exclamation'), ('헤헿', 'Exclamation'), ('엑', 'Exclamation'), ('흐음', 'Exclamation'), ('아싸', 'Exclamation'), ('네', 'Exclamation'), ('에구', 'Exclamation'), ('으아', 'Exclamation'), ('오', 'Exclamation'), ('흡', 'Exclamation'), ('헤헷', 'Exclamation'), ('헤헤', 'Exclamation'), ('그랬구나', 'Exclamation'), ('후우', 'Exclamation'), ('으이구', 'Exclamation'), ('호에', 'Exclamation'), ('으아아', 'Exclamation'), ('아자', 'Exclamation'), ('응가', 'Exclamation'), ('정말', 'Exclamation'), ('쳇', 'Exclamation'), ('헤에', 'Exclamation'), ('악', 'Exclamation'), ('예아', 'Exclamation'), ('아잉', 'Exclamation')], Mbti.J: [('내일', 'Noun'), ('일정', 'Noun'), ('약속', 'Noun'), ('계획', 'Noun')]}
