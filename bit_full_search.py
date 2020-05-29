from collections import deque
n = int(input())
for i in range(2**n):
    bitlist = deque()
    for j in range(n):
        if ((i >> j) & 1): #2進数表示のj桁目(0桁目から数える)が1かどうか
            bitlist.appendleft(1)
        else:
          	bitlist.appendleft(0)
    bitlist = list(bitlist)
    
