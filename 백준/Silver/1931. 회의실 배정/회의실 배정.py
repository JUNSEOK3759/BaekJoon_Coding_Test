import sys
input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

res = -2147483647
a.sort(key = lambda x : (x[1], x[0]))
cnt = 1
end_time = a[0][1]
for i in range(1, n):
    if a[i][0] >= end_time:
        cnt += 1
        end_time = a[i][1]
    
print(cnt)