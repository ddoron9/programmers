def solution(citations):
    answer = 0
    citations.sort()
    print(citations)
    for cur in range(max(citations)):  # 최대값까지 시도
        und = 0
        ov = 0
        for cit in citations:  # 배열 값 하나하나 넣음
            if cur <= cit:  # 현재 값보다 더 많이 인용된 수
                ov += 1
            if cur >= cit:  # 현재 값보다 더 적게 인용된 수
                und += 1
        if cur <= ov and cur >= und:  # h-index 값 만족하면 답에 입력
            answer = cur
    return answer
