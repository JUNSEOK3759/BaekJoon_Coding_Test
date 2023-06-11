def solution(a):
    a.sort()
    for i in range(len(a)-1):
        if a[i] == a[i+1][:len(a[i])]:
            return False
    else:
        return True