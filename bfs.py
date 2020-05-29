from collections import deque
cmd = [[-1,0],[1,0],[0,1],[0,-1]]
h,w = map(int,input().split())
sy,sx = map(int,input().split())
gy, gx = map(int,input().split())
sx -= 1
sy -= 1
gy -= 1
gx -= 1
Map = [list(input()) for _ in range(h)]
q = deque([[sx,sy]])
visidat = [[-1]*w for _ in range(h)]
visidat[sy][sx] = 0
while len(q) != 0:
    x,y = q.popleft()
    for cx,cy in cmd:
        newx = x + cx
        newy = y + cy
        if Map[newy][newx] == "#":
            continue
        else:
            if visidat[newy][newx] == -1:
                visidat[newy][newx] = visidat[y][x] + 1
                q.append([newx,newy])
print(visidat[gy][gx])