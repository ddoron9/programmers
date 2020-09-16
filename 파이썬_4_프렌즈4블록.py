

def solution(m, n, board):
    import numpy as np
    answer = 0
    x = [""] 
    for i in range(0,m): #문자열 list로 변환
        board[i] = list(board[i])
    board.reverse()
    board = np.transpose(board) #층별로 하나의 리스트로 만들어주기 위해 transpose
    board = board.tolist()  #array 를 리스트로 변환 
    while x:    #터트릴 행열 번호를 넣을 리스트
        del x[:] #while문에 들어왔으니 x 비워줌 
        for i in range(0,n-1): 
            for j in range(0,len(board[i])-1):
                if board[i][j] == "0":
                    pass
                elif(board[i][j] == board[i+1][j] and board[i+1][j+1] == board[i][j] and board[i][j+1]== board[i][j]):
                    #2x2 정사각형이 같은 모양일 때
                    for a in range(i,i+2):
                        for b in range(j,j+2): #x 에 값 추가
                            x.append((a,b))
        x = list(set(x)) #set 변환으로 중복을 제거하고 다시 리스트 casting
        x.sort(key=lambda x:x[1],reverse =True) #위 부터 제거해야 인덱스가 꼬이지 않으므로 정렬 열 값을 내림차순 정렬
        for a,b in x:  
            del board[a][b] #보드 값 제거 
            board[a].append("0") #연산에서 인덱스 범위를 보장해주기 위해 0 padding
        answer += len(x) #지운 수 answer에 더해줌
    return answer
