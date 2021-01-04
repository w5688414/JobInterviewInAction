

def z_naive(s):
    Z = [len(s)]
 
    for k in range(1, len(s)):
        n = 0
        while n + k < len(s) and s[n] == s[n + k]:
            n += 1
        Z.append(n)
 
    return Z

def Z_algorithm(s):
    N = len(s)
    Z_alg = [0]*N

    Z_alg[0] = N
    i = 1
    j = 0
    while i < N:
        while i+j < N and s[j] == s[i+j]:
            j += 1
        Z_alg[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < N and k + Z_alg[k]<j:
            Z_alg[i+k] = Z_alg[k]
            k += 1
        i += k
        j -= k
    return Z_alg

def get_z(s):
    l=0
    r=0
    n=len(s)
    z=[0]*n
    for i in range(1,n):
        if(i>r):
            l=i
            r=i
            while(r<n and s[r-l]==s[r]):
                r+=1
            z[i]=r-l
            r-=1
        else:
            k=i-l
            if(z[k]<r-i+1):
                z[i]=z[k]
            else:
                l=i
                while(r<n and s[r-l]==s[r]):
                    r+=1
                z[i]=r-l
                r-=1
    return z


def get_z_v1(s):
    n=len(s)
    l=0
    r=0
    z=[0]*n
    for i in range(n):
        if(i<=r):
            z[i]=min(r-i+1,z[i-l])
        while(i+z[i]<n and  s[z[i]]==s[z[i]+i]):
                z[i]+=1
        if(z[i]+i-1>r):
            l=i
            r=z[i]+i-1
    return z

if __name__ == "__main__":
    s='abcabc'
    res=z_naive(s)
    print(res)
    res=Z_algorithm(s)
    print(res)
    res=get_z(s)
    print(res)
    res=get_z_v1(s)
    print(res)