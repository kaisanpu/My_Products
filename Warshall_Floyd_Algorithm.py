#計算量V**3,pypyのほうが早い
V,E = map(int,input().split())#頂点、辺の数
INF = float("inf")
cost = [[INF]*V for _ in range(V)]#iからjへの重み付き距離cost[i][j]
for i in range(V):
    cost[i][i] = 0
for _ in range(E):
    s,t,dd = map(int,input().split())
    cost[s][t] = dd
#実装
for k in range(V):
    for i in range(V):
        for j in range(V):
            cost[i][j] = min(cost[i][j],cost[i][k]+cost[k][j])

for i in range(V):
    print(cost[i])
