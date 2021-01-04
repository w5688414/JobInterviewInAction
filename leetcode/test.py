
class Solution:
    def pancakeSort(self, arr: list) :
        
        def flip(sublist,k):
            i=0
            while(i<k/2):
                sublist[i],sublist[k-i-1]=sublist[k-i-1],sublist[i]
                i+=1
        
        ans=[]
        value_to_sort=len(arr)
        while(value_to_sort>0):
            # locate the position for the value to sort in this round
            index=arr.index(value_to_sort)
            
            if(index!=value_to_sort-1):
                # flip the value to the head if necessary
                if(index!=0):
                    ans.append(index+1)
                    flip(arr,index+1)
                    print(arr)
                
                ans.append(value_to_sort)
                flip(arr,value_to_sort)
                print(arr)
            value_to_sort-=1
            
        return ans
        

if __name__ == "__main__":
    solution=Solution()
    arr = [3,2,4,1]
    ans=solution.pancakeSort(arr)
    print(ans)
