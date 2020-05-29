from sys import stdin
input = stdin.readline

N = int(input())
WHITE = 0
GRAY = 1
BLACK = 2

M = [[0]*N for _ in range(N)]
color = [WHITE]*N  # colorの初期化は最初に行っておく。
d = [0]*N
f = [0]*N

def dfs_visit(u):
    global tt
    color[u] = GRAY
    tt += 1
    d[u] = tt # 最初の訪問
    for v in range(N):
        if M[u][v] == 0:
            continue
        if color[v] == WHITE:
            dfs_visit(v)
    color[u] = BLACK
    tt += 1
    f[u] = tt # 訪問の完了

def dfs():
    global tt
    tt = 0

    for u in range(N):
        if color[u] == WHITE:
            # 未訪問のuを始点として深さ優先探索
            dfs_visit(u)
    for u in range(N):
        print(str(u+1) + ' ' + str(d[u]) + ' ' + str(f[u]))
for _ in range(N):
    u, k, *vv = input().split()
    u = int(u)-1  # 0オリジンにする
    k = int(k)    # kは使わない
    for v in vv:
        v = int(v)-1
        M[u][v] = 1
dfs()