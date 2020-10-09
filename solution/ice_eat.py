# 음료수 얼려 먹기
"""
N x M 크기의 얼음 틀이 있고, 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다, 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램 작성

00110
00011
11111
00000
위 예시에서는 3개의 아이스크림이 만들어 진다.

입력 예시
4 5
00110
00011
11111
00000

출력 예시
3

해결 아이디어는 다음과 같다.
1. 특정한 지점의 주변 상, 하, 좌, 우 살펴본 뒤 주변 지점 중에 0이면 해당 지점 방문
2. 방문한 지점에서 다시 상, 하, 좌, 우 살펴 본 후 과정을 반복하면 연결된 모든 지점에 방문
3. 모든 노드에 대해 1~2번의 과정을 반복하며 방문하지 않은 지점의 수를 카운트
"""

n, m = map(int, input().split()) # 공백 기준으로 구분하여 입력받기

# 2차원 리스트의 맵 정보 입력 받기
ice_map = []
for i in range(n):
    ice_map.append(list(map(int, input())))
    

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 현재 노드를 아직 방문하지 않았다면
    if ice_map[x][y] == 0:
        ice_map[x][y] = 1 # 해당 노드 방문 처리
        
        #상, 하, 좌, 우의 위치들도 모두 재귀적을 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    return False


# 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result+=1
print(result)
