def solution(s):
    maxi = -2147483647
    mini = 2147483647
    for i in s.split():
        x = int(i)
        if x > maxi:
            maxi = x
        if x < mini:
            mini = x
    answer = str(mini) + ' '+ str(maxi)
    return answer