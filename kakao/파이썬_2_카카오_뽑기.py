def solution(board, moves):
    answer = 0
    stk = [] 
    for i in moves:       
        for j in range(0,len(board)): 
            #빈 공간이면 스킵
            if board[j][i-1] == 0: 
                continue
            #그게 아니면 
            #stack이 비거나 아랫 것과 다르면 추가
            if len(stk)==0 or board[j][i-1] != stk[-1]: 
                stk.append(board[j][i-1]) 
            #스택의 바로 아랫것과 같으면 터트림
            else: 
                stk.pop() 
                answer += 1     
            #뺐으니 빈 공간으로 만듬      
            board[j][i-1] = 0
            break
            
    return answer*2