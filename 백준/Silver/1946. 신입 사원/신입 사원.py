import sys
# sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)

n = int(input())

for _ in range(n):
    
    m = int(input())
    a = []
    for _ in range(m):
        a.append(list(map(int, input().split())))
    a.sort(key = lambda x : (x[0], x[1]))
    res = 1
    x = a[0][1]
    for i in range(1, len(a)):
        if a[i][1] < x:
            res += 1
            x = a[i][1]

    print(res)