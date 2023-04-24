def solution(n, k):
    deq = ''
    while n:
        deq = str(n%k) + deq
        n = n//k
    print(deq)
    deq = deq.split('0')
    cnt = 0
    for i in deq:
        if len(i) == 0:
            continue
        if int(i) == 1:
            continue
        prime = True
        for j in range(2, int(float(i) ** (1/2))+1):
            if int(i)%j == 0:
                prime = False
                break
        if prime:
            cnt += 1
    return cnt