s = "my name is jungsoo kim"

def solution(sentence):
    a = set(list(sentence))
    words = list(a)

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    answer_list = []

    for i in alphabet:
        if i not in words:
            answer_list.append(i)

    answer ="".join(answer_list)

    return answer

print(solution(s))