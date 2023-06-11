def solution(players, callings):
    dic = {v:k for k,v in enumerate(players)}
    
    for calling in callings:
        pre, now = dic[calling]-1, dic[calling]
        # dic만 사용하는 것이 아니라, 기존에 주어진 players 배열도 사용해야 하는 문제
        # 파이썬에서는 tmp 처리 안해도 swap 가능
        players[pre], players[now] = players[now], players[pre]
        dic[players[pre]], dic[players[now]] = dic[players[pre]] - 1 , dic[players[now]] + 1
        
    # dic의 키값을 return 하는 것이 아니라, players를 return 하는 것에 주의
    return players

'''
    시간초과 오류로 실패
    for call_name in callings:
        tmp = players.index(call_name)
        tmp_content = players[tmp]
        players[tmp] = players[tmp-1]
        players[tmp-1] = tmp_content
'''
