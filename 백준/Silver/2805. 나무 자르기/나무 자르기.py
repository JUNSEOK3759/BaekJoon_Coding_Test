def cut(mid, a):
    sum = 0
    for i in a:
        if i > mid:
            sum += i - mid
    return sum

n, m = map(int, input().split())

a = list(map(int, input().split()))
res = 0

lt = 0
rt = max(a)

while lt <= rt:
    mid = (lt + rt) // 2
    
    if cut(mid, a) >= m:
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1

print(res)