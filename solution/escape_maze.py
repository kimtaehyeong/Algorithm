# 미로 탈출

"""
동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혔습니다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
동빈이의 위치는 (1,1) 이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니다.
이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다. 미로는 반드시 탈출 가능하다!
이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산해라

입력 예시
5 6
101010
111111
000001
111111
111111

출력 예시
10
"""

from collections import deque

N, M = map(int, input().split(' '))

maze_map = []
for i in range(N):
    maze_map.append(list(map(int, input())))
    
    
# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


queue = deque()
queue.append((0,0)) # 처음 위치를 queue에 넣어준다.

# queue가 빌 때까지 반복
while queue:
    x, y = queue.popleft()
    
    # 4가지 방향으로 위치 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 벗어난 경우, 벽인 경우 무시
        if nx < 0 or ny < 0 or nx >= N or ny >= M or maze_map[nx][ny]==0:
            continue
        
        # 해당 위치를 처음 방문하는 경우에만 최단 거리 기록
        if maze_map[nx][ny] == 1:
            maze_map[nx][ny] = maze_map[x][y] + 1
            queue.append((nx, ny))
        
        

print(maze_map[N-1][M-1])