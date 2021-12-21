def solution(board, moves):
    big_lst = []
    lst = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] != 0:
                lst.append(board[j][i])
        lst.reverse()
        big_lst.append(lst)
        lst = []
    
    result_lst = []
    answer = 0
    moves.reverse()
    
    for j in range(len(moves)):
        num = moves.pop()
        if big_lst[num-1] != []:
            select = big_lst[num-1].pop()
            if result_lst == []:
                result_lst.append(select)
            elif select == result_lst[len(result_lst)-1]:
                result_lst.pop()
                answer += 2
            else:
                result_lst.append(select)
        else:
            continue
        print(result_lst)
            
    return answer

a = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
b = [1,5,3,5,1,2,1,4]

print(solution(a,b))
