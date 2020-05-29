#エラトステネス　計算量nlog(logn)
def primes(n):#nまでの素数を列挙0は入れちゃダメ
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,int(n**(0.5)+1)):
        if not is_prime[i]:
            continue
        for j in range(i*2,n+1,i):
            is_prime[j] = False
    return is_prime
def isprime(n):#nが素数か判定
    c = 1
    if n == 0 or n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        for i in range(2,int(n**(0.5)+1)):
            if n % i == 0:
                c = 0
                break
        return c