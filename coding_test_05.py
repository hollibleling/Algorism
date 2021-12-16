# 백준 알고리즘 2798 번 문제

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

lst_1 = []

for i in numbers:
    if i <= m // 3:
        lst_1.append(i)

answer_lst = []

for idx_1, number_1 in enumerate(lst_1):
    lst_2 = numbers[idx_1 + 1:]
    for idx_2, number_2 in enumerate(lst_2):
        lst_3 = lst_2[idx_2 + 1:]
        for number_3 in lst_3:
            val = number_1 + number_2 + number_3
            if val <= m:
                answer_lst.append(val)

answer_lst.sort()
print(answer_lst[len(answer_lst)-1])
