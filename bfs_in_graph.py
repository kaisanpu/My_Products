N,M = map(int,input().split())
Map = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    Map[a-1].append(b-1)
    Map[b-1].append(a-1)
sign = [0]*N
depth = [-1]*N
depth[0] = 0
q = deque([0])
while len(q) != 0:
    cur = q.popleft()
    for chi in Map[cur]:
        if depth[chi] != -1:
            continue
        depth[chi] = depth[cur]+1
        sign[chi] = cur
        q.append(chi)