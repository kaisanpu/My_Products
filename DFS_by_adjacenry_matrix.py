import sys
sys.setrecursionlimit(10 ** 10)
N,Q = map(int,input().split())
tree = [[] for _ in range(N)]
for _ in range(N):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
def dfs(cur,parent):
    li = tree[cur]
    for chi in li:
        if chi == parent:
            continue
        dfs(chi,cur)