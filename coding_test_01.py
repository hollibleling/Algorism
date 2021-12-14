def solution(new_id):
    
    a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    b = ["'", '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '[', '{', ']', '}', ':', '?', ',', '<', '>', '/']
    
    id_list = list(new_id)
    new_id_list = []
    
    for idx, i in enumerate(id_list):
        if i in a:
	        id_list[idx] = i.lower()
        if i in b:
            id_list[idx] = ''
        # if i == '.' and id_list[idx+1] == '.':
        #     id_list[idx] = ''
    
    i =0
    while i < len(id_list)-1:
        if id_list[i] == '.' and id_list[i+1] == '.':
            id_list[i] = ''
        i += 1
    
    for i in id_list:
        if i != '':
            new_id_list.append(i)
    
    print(new_id_list)

    for i in new_id_list:
        if new_id_list[0] == '.':
            del new_id_list[0]
        
    if new_id_list == []:
        new_id_list.append('a')
    
    for i in new_id_list:
        if new_id_list[len(new_id_list)-1] == '.':
            del new_id_list[len(new_id_list)-1]
    
    if len(new_id_list) >= 16:
        for i in range(15, len(new_id_list)):
            del new_id_list[15]
        if new_id_list[14] == '.':
            del new_id_list[14]
    
    if len(new_id_list) <= 2:
        word = new_id_list[len(new_id_list)-1]
        while len(new_id_list) < 3:
            new_id_list.append(word)
        
    answer = ''.join(new_id_list)
    return answer

print(solution("z-+.^."))

# bat.y.abcdefghi