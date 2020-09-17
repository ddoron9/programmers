def solution(priorities, location):
    answer = 0 
    from collections import deque
    priorities = deque(priorities)
    mine = priorities[location]
     
    while True:
        p = priorities[0] 
        if p != max(priorities):   
            priorities.append(p)
        else :
            answer+= 1
            if mine == max(priorities) and location == 0:
                break
        location -= 1
        if location < 0 : 
            location += len(priorities)-1
        priorities.popleft() 
    return answer
