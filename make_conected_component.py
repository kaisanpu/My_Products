#fr = [[] for _ in range(N)]
used = [-1]*N #-1なら未探索。数字はrenketuのindex
renketu = []
index = 0
def dfs(fr,cur,parent,index,li):
    children = fr[cur]
    for chi in children:
        if chi == parent or used[chi] != -1:
            continue
        used[chi] = index
        li.append(chi)
        dfs(fr,chi,cur,index,li)
for i in range(N):
    if used[i] != -1:
        continue
    li = [i]
    used[i] = index
    dfs(fr,i,-1,index,li)
    index += 1
    renketu.append(li)
