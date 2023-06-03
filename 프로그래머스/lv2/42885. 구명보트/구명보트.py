def solution(people, limit):
    i, answer = 0, 0
    people.sort()
    end = len(people) - 1
    
    for i in range(int(len(people)/2)):
        while(i < end):
            if((people[i] + people[end]) <= limit):
                answer += 1
                end -= 1
                break
            else:
                end -= 1
                continue
    answer += (len(people) - (answer*2))
    return answer