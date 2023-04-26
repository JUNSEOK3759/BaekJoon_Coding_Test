import sys
# sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)

n = int(input())

a = []

for _ in range(n):
    a.append(list(map(int, input().split())))
    
a.sort(key = lambda x : (x[1], x[0]))

time = 0
cnt = 0
for i in a:
    if i[0] >= time:
        time = i[1]
        cnt += 1
print(cnt)