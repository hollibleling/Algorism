n = int(input())
dots = list(map(int, input().split()))

sorted_dots = sorted(list(set(dots)))
print(sorted_dots)

dic = {}
for i in range(len(sorted_dots)):
    dic[sorted_dots[i]] = i

for j in dots:
    print(dic[j], end = ' ')







# sorted_dots = []
# for k in dots:
#     sorted_dots.append(k)

# sorted_dots.sort()

# new_dots = []
# for i in sorted_dots:
#     if i not in new_dots:
#         new_dots.append(i)

# answer = []
# for j in dots:
#     answer.append(new_dots.index(j))

# print(answer)
