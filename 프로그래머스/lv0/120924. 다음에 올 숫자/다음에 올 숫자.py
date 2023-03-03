def solution(common):
    if common[len(common)-1] - common[len(common)-2] == common[len(common)-2] - common[len(common)-3]:
        answer = common[len(common)-1] + (common[len(common)-1] - common[len(common)-2])
    else:
        answer = common[len(common)-1] * (common[len(common)-1] // common[len(common)-2])
    return answer