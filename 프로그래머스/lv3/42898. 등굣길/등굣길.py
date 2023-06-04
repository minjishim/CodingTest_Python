from collections import deque

def solution(m, n, puddles):
    answer = 0
    graph = [[0] * m for _ in range(n)]
    graph[0][0] = 1

    '''
    line 10~11을 이렇게 하고, line 16을 graph[i][j] == 1 로 하게 되면, puddle이 아닌데 1인 경우 때문에 오류가 생김
    for i in range(len(puddles)):
        graph[puddles[i-1][1]-1][puddles[i-1][0]-1] = 1
    '''
    
    for i in range(0, n):
        for j in range(0, m):
            # if(graph[i][j] == 1):
            if([j+1, i+1] in puddles or [i, j] == [0, 0]):  # puddles는 x, y 좌표가 거꾸로
                                                            # puddles의 경우에는 (0, 0)부터가 아닌 (1, 1)부터 시작이므로 +1씩
                continue
            else:
                graph[i][j] = graph[i-1][j] + graph[i][j-1]
                
    return (graph[-1][-1] % 1000000007)
