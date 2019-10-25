# https://programmers.co.kr/learn/courses/30/lessons/43105 정수 삼각형

def solution(triangle):
    answer = 0
    n = len(triangle)
    for i in range(n-1 , 0, -1):
        if i == 0 :
            break;
        for j in range (0, i):
            if (triangle[i][j]) > (triangle[i][j+1]) :
                triangle[i-1][j] = (triangle[i-1][j]) + (triangle[i][j])
            else :
                triangle[i-1][j] = (triangle[i-1][j]) + (triangle[i][j+1])
    answer = triangle[0][0]
    return answer