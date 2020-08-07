def solution(x, n):
    end = x*n #리스트 마지막 항
    if x<0: 
        end -= 1
    elif x>0: 
        end += 1
    else: #0일 때
        return [0 for _ in range(n)]
    
    answer = [i for i in range(x,end,x)]
    return answer