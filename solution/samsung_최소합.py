def dfs(y, x):
    global sub_result, result
    
    if result < sub_result:
        return
    
    if y == test -1 and x == test-1:
        result = sub_result
        return
    
    for i in range(2):
        dy = y + move_y[i]
        dx = x + move_x[i]
        
        
        if 0<=dy<test and 0<=dx<test and (dy,dx) not in check:
            check.append((dy, dx))
            sub_result += minumum_map[dy][dx]
            dfs(dy, dx)
            check.remove((dy, dx))
            sub_result -= minumum_map[dy][dx]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    test = int(input())
    minumum_map = [list(map(int, input().split())) for _ in range(test)]
    check = []
    move_x = [1, 0]
    move_y = [0, 1]
    sub_result, result = minumum_map[0][0], 1000000
    dfs(0,0)   
    print('#%d %d'%(test_case, result))