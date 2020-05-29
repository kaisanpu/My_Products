#計算量ElogV
V,E,r = map(int,input().split()) #頂点数、辺の数，始点
cost = [[] for _ in range(V)] #cost[u][v]がuからvへの距離
INF = float("inf")
d = [INF]* V #頂点ｒから頂点iへの最短重み距離　　　　　
prev = [-1] * V #最短距離をたどるとき、頂点iの一回前に通る頂点
used = [True]*V #Trueは未確定
for _ in range(E):
    s,t,dd = map(int,input().split())
    cost[s].append([dd,t])
d[r] = 0
used[r] = False
#実装
import heapq
Q = []
for e in cost[r]:
    heapq.heappush(Q,e)
pr = r
while len(Q) != 0:
    dis,v = heapq.heappop(Q)
    if used[v] == False:#すでに確定していたら
        continue
    prev[v] = pr
    pr = v
    d[v] = dis
    used[v] = False #確定させる
    for e in cost[v]:
        if used[e[1]] == True:#まだ確定していなかったら
            heapq.heappush(Q,[e[0]+d[v],e[1]])
for k in d:
    if k != INF:
        print(k)
    else:
        print("INF")






