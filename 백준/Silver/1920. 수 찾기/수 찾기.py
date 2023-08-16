n = int(input())
b = list(map(int, input().split()))
b.sort()
m = int(input())
a = list(map(int, input().split()))

for i in a:
    lt = 0
    rt = n-1
    
    while lt <= rt:
        mid = (lt + rt) // 2
        if b[mid] == i:
            print(1)
            break
        elif b[mid] > i:
            rt = mid -1
        else:
            lt = mid + 1
    else:
        print(0)