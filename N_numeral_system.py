def solution(n, t, m, p):
    # n 진법 t 개 m 인원 p 순서
    answer = ''
    st = list('0123456789ABCDEF')
    num = 0
    lst = ['0']

    # t개 되면 멈춤
    while len(answer) < t:

        i = num  # 현재 진법을 바꿀 숫자
        tmp = []  # n진법으로 바뀐 숫자 리스트
        while i > 0:
            tmp.insert(0, st[i % n])
            i = int(i/n)

        if num != 0:
            lst.extend(tmp)  # lst에 추가

        # 현재 차례가 왔을 때 p == m 일 경우엔 나머지가 0 이므로
        if p == (num+1) % m or (p == m and (num+1) % m == 0):  # 현재 차례 수
            answer += lst.pop(0)
        # 딴사람 차례
        else:
            lst.pop(0)

        num += 1
    return answer
