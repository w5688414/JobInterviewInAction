class Solution:
    def isRobotBounded(self, instructions: str):
        d=0
        x=0
        y=0
        all_direction = [[0,1],[1,0],[0,-1],[-1,0]] # 方向: 0上   1右   2下   3左
        for j in range(4):
            for i in instructions:
                if(i=='L'):
                    d-=1
                elif(i=='R'):
                    d+=1
                else:
                    x+=all_direction[d%4][0]
                    y+=all_direction[d%4][1]
                    print(x,y)
        return x==0 and y==0

if __name__ == "__main__":
    solution=Solution()
    s='GGLLGG'
    res=solution.isRobotBounded(s)
    print(res)