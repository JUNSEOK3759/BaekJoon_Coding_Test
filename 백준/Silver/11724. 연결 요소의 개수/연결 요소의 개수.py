import sys
sys.setrecursionlimit(10**6) # 재귀 허용 깊이를 수동으로 늘려주는 코드

# dfs 탐색
def dfs(x):

    visited[x] = True

    # 탐색하지 않은 연결된 노드 찾기
    for i in range(1, n+1):
        if graph[x][i] == 1 and visited[i] == False:
            dfs(i)


n, m = map(int, sys.stdin.readline().split())

# 노드 탐색 유무
visited = [False] * (n + 1)

graph = [[0] * (n + 1) for i in range(n + 1)]
# 2차원 리스트의 맵 정보를 입력 받는다.
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b][a] = graph[a][b] = 1

cnt = 0

# 현재 위치에서 DFS 수행
for i in range(1, n + 1):
    if visited[i] == False:
        dfs(i)
        cnt += 1
print(cnt)