import math

class Solution:
    def __init__(self):
        super().__init__()
        self.corners=[]
        self.ths=[]
    def find_level(self,num):
        return math.floor(math.log(num,2))
    
    def find_parent(self,label):
        level=self.find_level(label)
        corner=2**level
        th=(label-corner)//2+1
        self.corners.append(corner)
        self.ths.append(th)
        return corner-1-th+1
        
    def pathInZigZagTree(self, label):
        res=[label]
        while(True):
            label=self.find_parent(label)
            if(label>=1):
                res.append(label)
            else:
                return res[::-1]
        

if __name__ == "__main__":
    solution=Solution()
    res=solution.pathInZigZagTree(14)
    print(res)
    print(solution.corners)
    print(solution.ths)