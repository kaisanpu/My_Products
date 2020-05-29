H,W = map(int,input().split())
Map = [["."]*(W+2)]
for _ in range(H):
    Map.append(["."]+list(input())[:-1] + ["."])
Map.append(["."]*(W+2))
for i in range(H+2):
    print(Map[i])