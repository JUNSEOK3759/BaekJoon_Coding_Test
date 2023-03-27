def solution(answers):
    answer = []
    num1 = [1, 2, 3, 4, 5] * 2000
    num2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    cnt1 = cnt2 = cnt3 = 0
    for index, value in enumerate(answers):
        if num1[index] == value:
            cnt1 += 1
        if num2[index] == value:
            cnt2 += 1
        if num3[index] == value:
            cnt3 += 1
    if max(cnt1, cnt2, cnt3) == cnt1:
        answer = [1]
    elif max(cnt1, cnt2, cnt3) == cnt2:
        answer = [2]
    else:
        answer = [3]
    
    if cnt1 == cnt2 and cnt1 > cnt3:
        answer = [1, 2]
    elif cnt1 == cnt3 and cnt1 > cnt2:
        answer = [1, 3]
    elif cnt2 == cnt3 and cnt2 > cnt1:
        answer = [2, 3]
    if cnt1 == cnt2 == cnt3:
        answer = [1, 2, 3]
    
    
        
    return answer