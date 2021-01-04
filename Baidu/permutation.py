

def solve(arr,cur,ans,visited,res):
    if(cur==len(arr)):
        t=[item for item in ans]
        res.append(t)
    for i in range(len(arr)):
        if(visited[i]==False):
            ans.append(arr[i])
            visited[i]=True
            solve(arr,cur+1,ans,visited,res)
            visited[i]=False
            ans.pop(-1)

if __name__ == "__main__":
    arr=[1,2,3,4]
    res=[]
    visited=[False]*len(arr)
    solve(arr,0,[],visited,res)
    print(res)
    print(len(res))
