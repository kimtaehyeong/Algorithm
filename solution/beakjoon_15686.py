from itertools import combinations

n,m = map(int, input().split())
chicken_map = []
for _ in range(n):
    a = list(map(int, input().split(' ')))
    chicken_map.append(a)
    

chicken = []
home = []
for i in range(n):
    for j in range(n):
        if chicken_map[i][j] == 1:
            home.append([i,j])
        if chicken_map[i][j] == 2:
            chicken.append([i,j])
            

k = list(combinations(chicken,m))

def distance(chicken, home):
    min_dist = 50000
    for chi in chicken:
        z = abs(chi[0] - home[0]) + abs(chi[1] - home[1])
        #print(z)
        min_dist = min(min_dist, z)
    return min_dist



solution = []
for chi in k:
    total = 0
    for hm in home:
        total = total + distance(chi, hm)
    solution.append(total)

print(min(solution))