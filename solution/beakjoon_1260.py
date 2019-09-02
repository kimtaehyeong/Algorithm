# https://www.acmicpc.net/problem/1260
# DFS와 BFS

n, m, start_v = map(int, input().split(' ')) # 정점, 간선, 시작번호

adj_list = [[] for _ in range(n+1)]
check_list = [False] * (n+1)


for _ in range(m):
    u, v = map(int, input().split(' '))
    adj_list[u].append(v) # 양 방향 그래프
    adj_list[v].append(u)

for k in range(n):
    adj_list[k].sort() # 순서를 정렬할 필요는 없지만 문제에서 낮은 순서부터 방문
    
    
def dfs(x):
    global check_list
    check_list[x] = True
    print(x, end=' ')
    for y in adj_list[x]:
        if check_list[y] == False:
            dfs(y)

def bfs(x):
    check_list = [False] * (n+1)
    q = []
    q.append(x)
    check_list[x] = True
    while q:
        value_x = q.pop(0)
        print(value_x, end=' ')
        for j in adj_list[value_x]:
            if check_list[j] == False:
                check_list[j] = True
                q.append(j)
dfs(start_v)
print()
bfs(start_v)