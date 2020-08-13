# https://programmers.co.kr/learn/courses/30/lessons/12951
# JadenCase 문자열 만들기


def solution(s):
    answer = ''
    for w in s:
         # 첫 글자나 앞 글자가 공백일 때
        if len(answer) == 0 or answer[-1] == ' ':
            answer += w.upper()
        else:
            answer += w.lower()
    return answer
