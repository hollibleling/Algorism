from itertools import combinations

def solution(M, load, answer = 0):
    load.sort()
    a = len(load)

    if load == []:
        return answer

    if max(load) > M:
        return -1
    
    
    for i in range(len(load)):
        combi = list(combinations(load, a-i))
        combi.reverse()
        for k in combi:
            if sum(k) <= M:
                if load == []:
                    break
                answer +=1
                # print(k)
                for num in k:
                    if num in load:
                        load.remove(num)
                        # print(load)
                answer = solution(M, load, answer)
                # print(answer)
    return answer

print(solution(20, [1, 3, 9, 15, 16, 17]))
print(solution(5, [2, 2, 2, 2, 2]))
print(solution(10, [1, 5, 6, 7, 9, 10]))

