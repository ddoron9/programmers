def solution(numbers, target):
    from collections import deque

    # numbers 리스트 값과 , 깊이를 튜플로 넣어줌
    queue = deque([(numbers[0], 0), (-numbers[0], 0)])

    while queue:
        # bfs
        node = queue.popleft()

        # break 문 역할 > 마지막에는 target 값을 합으로 갖는 마지막 깊이의 개수 return
        if node[1] == len(numbers)-1:
            return queue.count((target, len(numbers)-1))

        # 자식 노드 전달
        children = [(node[0]+numbers[node[1]+1], node[1]+1),
                    (node[0]-numbers[node[1]+1], node[1]+1)]
        queue.extend(children)
