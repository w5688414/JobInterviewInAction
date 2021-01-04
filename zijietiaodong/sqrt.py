

def solve(x,ratio):
    num=x
    while(True):
        num=(num+x/num)/2
        if(abs(x-num*num)<=ratio):
            break
    return num

def binary_search(x,ratio):
    l=0
    h=x
    while(l<=h):
        mid=l+(h-l)/2
        if(mid*mid>x):
            h=mid
        elif(x-mid*mid<=ratio):
            return mid
        else:
            l=mid

if __name__ == "__main__":
    x=5
    ratio=0.01
    res=solve(x,ratio)
    print(res)
    res=binary_search(x,ratio)
    print(res)