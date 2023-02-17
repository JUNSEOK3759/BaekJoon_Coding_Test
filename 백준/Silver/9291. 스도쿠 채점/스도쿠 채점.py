def check(a):
    for i in range(9):
        res1 = [0 for _ in range(10)]
        res2 = [0 for _ in range(10)]
        for j in range(9):
            res1[a[i][j]] += 1
            res2[a[j][i]] += 1
        if max(res1) > 1 or max(res2) > 1:
            return False
    for i in range(3):
        for j in range(3):
            res3 = [0 for _ in range(10)]
            for k in range(3):
                for l in range(3):
                    res3[a[i*3+k][j*3+l]] += 1     
            if max(res3) > 1:
                return False        
    return True
n = int(input())
for z in range(n):
    a = [0 for _ in range(9)] 
    q = 9
    while True:
        if q == 0:
            break
        x = list(map(int, input().split()))
        if x:
            a[9-q] = x
        else:
            continue
        q -= 1

    if check(a):
        print(f'Case {z+1}: CORRECT')
    else:
        print(f'Case {z+1}: INCORRECT')