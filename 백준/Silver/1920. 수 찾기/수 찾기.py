import sys
# sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)

n = int(input())

a = list(map(int, input().split()))
a.sort()

m = int(input())

b = list(map(int, input().split()))

for i in range(len(b)):
    lt = 0      
    rt = n-1            
    while lt <= rt:
        mid = (lt + rt) // 2
        if a[mid] == b[i]:
            print(1)
            break
        else:
            if b[i] > a[mid]:
                lt = mid + 1
            else:
                rt = mid -1
    else:
        print(0)
