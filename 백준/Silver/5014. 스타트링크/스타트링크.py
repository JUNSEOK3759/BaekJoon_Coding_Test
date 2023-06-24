import sys
from collections import deque, Counter

# sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)

def bfs(n):
    dq = deque()
    dq.append(n)
    while dq:
       x = dq.popleft()
       if x == g:
           print(ch[x]-1)
           sys.exit(0)
       for next in (x+u, x-d):
            if 0 < next < f+1 and ch[next] == 0:
                ch[next] = ch[x] + 1
                dq.append(next)

        
f, s, g, u, d = map(int, input().split())
if s == g:
    print(0)
    sys.exit(0)
ch = [0 for _ in range(f+1)]
ch[s] = 1
bfs(s)
print('use the stairs')