#pythonのほうが早い powだけだとpypyのほうが早い
MOD = 10**9 + 7
def comb(n, k, mod):
    if n<0 or k<0 or n<k:
        return 0
    if n==0 or k==0:
        return 1
    k=k if k<=n-k else n-k
    x = 1
    y = 1
    for i in range(k):
        x=x*(n-i)%mod
        y=y*(i+1)%mod
    return (x*pow(y,mod-2,mod))%mod
#こっちは計算量O(N) comb_mod = O(1),maketable = O(N) 
fac = [1, 1]
inv = [0, 1]
finv = [1, 1]
for i in range(2, N+1):
    fac.append(fac[-1] * i % MOD)
    inv.append(MOD - inv[MOD%i] * (MOD//i) % MOD)
    finv.append(finv[-1] * inv[-1] % MOD) 
def comb_mod(n, r, m):
    if (n<0 or r<0 or n<r): return 0
    r = min(r, n-r)
    return fac[n] * finv[n-r] * finv[r] % m