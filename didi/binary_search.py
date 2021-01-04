
class LeafNode():
    def __init__(self,val=0,left=None,right=None):
        super().__init__()
        self.left=left
        self.right=right
        self.val=val


def solve(root,target):
    if(root is None):
        return None
    if(target<root.val):
        root.left=solve(root.left,target)
    elif(target>root.val):
        root.right=solve(root.right,target)
    elif(target==root.val):
        if(root.left is None):
            root=root.right
        elif(root.right is None):
            root=root.left
        else:
            t=root.right
            while(t.left):
                t=t.left
            root.val=t.val
            root.right=solve(root.right,t.val)
    return root
    


