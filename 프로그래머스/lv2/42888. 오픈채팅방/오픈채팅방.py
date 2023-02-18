def solution(record):
    answer = []
    dic = {}
    for i in record:
        x = i.split()
        if x[1] in dic:
            if x[0] in ['Enter', 'Change']:
                dic[x[1]] = x[2]
            else:
                continue
        else:
            dic[x[1]] = x[2]

    for i in record:
        x = i.split()
        if x[0] == 'Enter':
            answer.append(f'{dic[x[1]]}님이 들어왔습니다.')
        elif x[0] == 'Leave':
            answer.append(f'{dic[x[1]]}님이 나갔습니다.')
        else:
            continue
    return answer