def solution(word):
    alpha = ["A", "E", "I", "O","U"]
    multiple = [781, 156, 31, 6, 1]
    answer = 0
    
    for i in range(len(word)):
        answer += (alpha.index(word[i]) * multiple[i]) + 1
    return answer
