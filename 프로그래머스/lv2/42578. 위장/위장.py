from collections import defaultdict

def solution(clothes):
    answer = 1
    d = defaultdict(int)
    for _, types in clothes:
        d[types] += 1
    for i in d.values():
        answer *= (i+1)
    return (answer - 1)
