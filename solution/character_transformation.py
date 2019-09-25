def bfs(V, Adj, s):
    level = {s:0}
    i = 1
    frontier = [s]
    while frontier:
        new = []
        for u in frontier:
            for v in Adj[V.index(u)]:
                if v not in level:
                    level[v] = i
                    new.append(v)
        frontier = new
        i += 1
    return level

def solution(begin, target, words):
    if target not in words: return 0
    words.insert(0, begin)
    Adj = []
    n = len(begin)
    for word in words:
        tmp = []
        for leftword in words:
            cnt = 0
            for i in range(n):
                if word[i] == leftword[i]: cnt += 1
            if cnt == n-1: tmp.append(leftword)
        Adj.append(tmp)
    answer_dict = bfs(words, Adj, begin)
    return answer_dict[target]
