def solution(prices):
    stk_price = [[prices[i], i] for i in range(len(prices))]
    time = 0
    stk = []
    answer = [0 for i in range(len(prices))]

    for i in range(len(stk_price)):
        while((len(stk) != 0) and (stk[-1][0] > stk_price[i][0])):
            answer[stk[-1][1]] = time - stk[-1][1]
            stk.pop()  
        if((len(stk) == 0) or (stk[-1][0] <= stk_price[i][0])):
            stk.append(stk_price[i])
        time += 1

    j = 0
    for i in range(len(answer)):
        if(answer[i] == 0):
            answer[i] = time - stk[j][1] - 1
            j += 1

    return answer