N = int(input())
M = [[0]*N for _ in range(N)]
for _ in range(N):
    nums = list(map(int,input().split()))
    a = nums[1]
    if a == 0:
        continue
    else:
        for j in nums[2:]:
            M[nums[0]-1][j-1] = 1
for i in range(N):
    print("".join(map(str,M[i])))