V,E = map(int,input().split())
dist = [[float("inf")]*V for _ in range(V)]
for i in range(E):
    s,t,d = map(int,input().split())
    dist[s][t] = d
dp = [[-1]*V for i in range(1<<V)] #dp[S][v]Sは訪れた町の集合vは今いる点
#訪れた集合がs、今いる点がvの時０に戻る最短経路
def rec(s,v,dp):
    if dp[s][v] >= 0:
        return dp[s][v]  #一度出てきたもの
        
    if s == (1<<V)-1 and v == 0:
        #全ての頂点を訪れた(s = 11...11 and v = 0)
        dp[s][v] = 0
        return 0
    
    res = float("inf")
    for u in range(V):
        if (s>>u&1) == 0:
            #uに訪れていない時(uの箇所が0の時),次はuとすると
            res = min(res,rec(s|(1<<u),u,dp)+dist[v][u])
            
    dp[s][v] = res
    return res
a = rec(0,0,dp)
if a == float("inf"):
    print(-1)
else:
    print(a)