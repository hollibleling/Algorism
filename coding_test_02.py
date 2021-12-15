n = int(input())

count = 0

for _ in range(n):
    word = input()
    error = 0

    for idx in range(len(word)-1):
        if word[idx] != word[idx+1]:
            new_word = word[idx+1:]
            if new_word.find(word[idx]) >= 0:
                error += 1
    if error == 0:
        count += 1

print(count)



# i = 0
# words = []
# while i < N:
#     if N > 100:
#         print("wrong input")
#         break
#     words.append(input())
#     i += 1

# print(words)

# for i in words:
#     word = i
#     n= 0
#     for idx, j in enumerate(word):
#         if j == word[idx+1]:
#             word.lstrip(j)
#         else:
#             word.lstrip(j)
#             if word == '':
#                 n += 1
#             elif word.find[j]:
#                 break
#             else:
#                 continue

# print(n)
                
            
