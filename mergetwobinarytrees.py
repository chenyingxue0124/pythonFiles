class Treenode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):       
    def mergeTree(self,t1,t2):
        if t1 and t2 :
            root = Treenode(t1.val + t2.val)
            root.left = self.mergeTree(t1.left,t2.left)
            root.right = self.mergeTree(t1.right,t2.right)  
            return root
        elif not t1 and not t2:
            return None
        else:
            return t1 or t2

if __name__=='__main__':
    print(Solution.mergeTree([1,2,3],[2,3,4],[]))