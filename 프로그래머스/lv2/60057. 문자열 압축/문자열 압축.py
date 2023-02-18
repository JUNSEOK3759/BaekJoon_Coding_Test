def solution(s):
    result=[]
    if len(s) == 1:
        return 1
    for i in range(1, (len(s) // 2) + 1):
        b = ''
        cnt = 1
        temp = s[:i]
        for j in range(i, len(s), i):
            if temp == s[j:j+i]:
                cnt += 1
            else:
                if cnt != 1:
                    b = b + str(cnt) + temp
                else:
                    b = b + temp
                temp = s[j:j+i]
                cnt = 1
        if cnt != 1:
            b = b + str(cnt) + temp
        else:
            b = b + temp
        result.append(len(b))
    return min(result)