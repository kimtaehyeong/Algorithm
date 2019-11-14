# www.acmicpc.net/problem/14502 연구소
# 일부 빈 칸에는 바이러스가 있고, 인접한 빈 칸으로 계속 펴져 나가는데,
# BFS, DFS로 문제를 해결할 수 있다.
# 모든 빈칸을 한번씩 다 방문을 해야되는 경우이므로, O(NM)이 걸린다.
# 하지만 여기서 벽을 3개 세워야 하니 NM^3이 걸린다.
# 총 NM^4 걸린다. 최악인 경우는..

from collections import deque

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a):
    n = len(a)
    m = len(a[0])
    b = [[0]*m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][j]
            if b[i][j] == 2:
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and b[nx][ny] == 0:
                b[nx][ny] = 2
                q.append((nx,ny))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                cnt += 1
    return cnt


for x1 in range(n):
    for y1 in range(m):
        if a[x1][y1] != 0:
            continue
        for x2 in range(n):
            for y2 in range(m):
                if a[x2][y2] != 0:
                    continue
                for x3 in range(n):
                    for y3 in range(m):
                        if a[x3][y3] != 0:
                            continue
                        if x1 == x2 and y1 == y2:
                            continue
                        if x1 == x3 and y1 == y3:
                            continue
                        if x2 == x3 and y2 == y3:
                            continue
                        a[x1][y1] = 1
                        a[x2][y2] = 1
                        a[x3][y3] = 1
                        cur = bfs(a)
                        if ans < cur:
                            ans = cur
                        a[x1][y1] = 0
                        a[x2][y2] = 0
                        a[x3][y3] = 0
print(ans)