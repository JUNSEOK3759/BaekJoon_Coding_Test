def solution(elements):
    # answer = set(elements)
    # a = 2
    # while a <= 5:
    #     for i in range(len(elements)):
    #         elements2 = elements[i : i+a]
    #         ele2_len = len(elements2)
    #         if ele2_len < a:
    #             elements2 = elements[i : i+a] + elements[0 :a - ele2_len]
    #         answer.add(sum(elements2))
    #     a+= 1
    # return len(answer)
    
    
    
    elements *= 2
    a = 1
    x = set()
    while a <= len(elements) // 2:
        for i in range(len(elements) // 2 + 1):
            x.add(sum(elements[i : i+a]))
        a+=1
    return len(x)



   
    
    
#     answer = 0
#     x = []
#     for i in range(2, len(elements) + 1):
#         for j in range(0, len(elements) -1, i):
#             print(elements[j : j+i])
#             x.append(sum(elements[j : j+i]))
    
#     return answer
