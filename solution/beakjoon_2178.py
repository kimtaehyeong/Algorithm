# https://www.acmicpc.net/problem/2178

n,m = map(int, input().split())

maze_map = [list(map(int, input())) for _ in range(n)]
check_list = [[0]*m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

q = []
q.append([0,0])
check_list[0][0] = 1

while len(q) != 0:
    x,y = q.pop(0)
    
    for i in range(4):
        fx = x + dx[i]
        fy = y + dy[i]
        
        if fx < 0 or fx>=n:
            continue
        if fy < 0 or fy>=m:
            continue
        if maze_map[fx][fy] == 0:
            continue
        if check_list[fx][fy] != 0:
            continue
        
        check_list[fx][fy] = check_list[x][y] + 1
        q.append([fx,fy])
        
print(check_list[n-1][m-1])