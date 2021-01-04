
import collections

class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def solve(root,K,preSum,level,l,d):
    if(root is None):
        return l
    curSum=preSum+root.val
    if(curSum not in d):
        d[curSum]=level
        # print(d)
    if(curSum-K in d):
        l=max(level-d[curSum-K],l)
    l=solve(root.left,K,curSum,level+1,l,d)
    l=solve(root.right,K,curSum,level+1,l,d)
    if(level==d[curSum]):
        d.pop(curSum)
    return l

def getMaxLength(root,K):
    d=collections.defaultdict(int)
    d[0]=0
    return solve(root,K,0,1,0,d)

if __name__ == "__main__":
    vals = [-3, 3, -9, 1, 0, 2, 1, 1, 6]
    nodes = [TreeNode(v) for v in vals]

    root = nodes[0]
    nodes[0].left, nodes[0].right = nodes[1], nodes[2]
    nodes[1].left, nodes[1].right = nodes[3], nodes[4]
    nodes[2].left, nodes[2].right = nodes[5], nodes[6]
    nodes[4].left, nodes[4].right = nodes[7], nodes[8]

    assert(getMaxLength(root, 6) == 4)
    assert(getMaxLength(root, -9) == 1)
    assert(getMaxLength(root, -10) == 3)
    assert(getMaxLength(root, -11) == 3)
    assert(getMaxLength(root, 4) == 3)
    assert(getMaxLength(root, 1) == 4)
    assert(getMaxLength(root, 3) == 2)