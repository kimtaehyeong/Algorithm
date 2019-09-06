# https://www.acmicpc.net/problem/13458

n = int(input()) # 시험장 갯수
a = list(map(int, input().split(' '))) # 응시자 수
b, c = map(int,input().split(' ')) # 총 감독관에 학생, 부 감독관 감시 학생 수


ans = 0

for j in range(n):
    z = 0
    z = a[j] - b
    if z <= 0:
        ans += 1
        pass
    else:
        z = a[j] - b
        ans += 1
        ze = z % c
        z = z // c
        ans += z
        if ze != 0:
            ans += 1
        
print(ans)
