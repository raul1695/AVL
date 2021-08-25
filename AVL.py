"""

This is my implementation of the AVL tree. 

I used the code and explenation found in : https://www.youtube.com/watch?v=lxHF-mVdwK8 and https://www.youtube.com/watch?v=jDM6_TnYIqE

for my implementation


"""



class TreeNode:
    def __init__(self, key = None):
        self.val = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1
    def __str__(self):
        return str(self.val)


class AVL:
    def __init__(self, key = None):
        self.root = None
    
    def insert(self,value):
        if self.root==None:
            self.root=TreeNode(value)
        else:
            self._insert(value,self.root)
    
    def _insert(self,value,cur_node):
        if value<cur_node.val:
            if cur_node.left==None:
                cur_node.left=TreeNode(value)
                cur_node.left.parent=cur_node # set parent
                self._inspect_insertion(cur_node.left)
            else:
                self._insert(value,cur_node.left)
        elif value>cur_node.val:
            if cur_node.right==None:
                cur_node.right=TreeNode(value)
                cur_node.right.parent=cur_node # set parent
                self._inspect_insertion(cur_node.right)
            else:
                self._insert(value,cur_node.right)
        else:
            print("Value already in tree!")

    def __height(self,node):
        if(node == None):
            return -1
            
        return max(self.__height(node.left) ,self.__height(node.right)) +1

    def getBalanceFactor(self,node):
        l = self.__height(node.left)
        r = self.__height(node.right)

        return l - r

    def getBalance(self):
        return self.getBalanceFactor(self.root)
        
    def _inspect_insertion(self,cur_node,path=[]):
        if cur_node.parent==None: 
            return
        path=[cur_node]+path
        left_height =self.get_height(cur_node.parent.left)
        right_height=self.get_height(cur_node.parent.right)

        if abs(left_height-right_height)>1:
            path=[cur_node.parent]+path
            self._rebalance_node(path[0],path[1],path[2])
            return
        new_height=1+cur_node.height 
        
        if new_height>cur_node.parent.height:
            cur_node.parent.height=new_height
        self._inspect_insertion(cur_node.parent,path)
        
    def get_height(self,cur_node):
        if cur_node==None: 
            return 0
        return cur_node.height
        
    def __print(self,node):
        if(node == None):
            return
        else:
            print(node)
            self.__print(node.left)
            self.__print(node.right)       
            return

    def print(self):
        self.__print(self.root)
    
    def _rebalance_node(self,z,y,x):
        if y==z.left and x==y.left:
            self._right_rotate(z)
        elif y==z.left and x==y.right:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y==z.right and x==y.right:
            self._left_rotate(z)
        elif y==z.right and x==y.left:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception('_rebalance_node: z,y,x node configuration not recognized!')
    
    def _right_rotate(self,z):
        sub_root=z.parent 
        y=z.left
        t3=y.right
        y.right=z
        z.parent=y
        z.left=t3
        if t3!=None: 
            t3.parent=z
        y.parent=sub_root
        if y.parent==None:
            self.root=y
        else:
            if y.parent.left==z:
                y.parent.left=y
            else:
                y.parent.right=y		
        z.height=1+max(self.get_height(z.left),self.get_height(z.right))
        y.height=1+max(self.get_height(y.left),self.get_height(y.right))
    
    def _left_rotate(self,z):
        sub_root=z.parent 
        y=z.right
        t2=y.left
        y.left=z
        z.parent=y
        z.right=t2
        if t2!=None: 
            t2.parent=z
        y.parent=sub_root
        if y.parent==None: 
            self.root=y
        else:
            if y.parent.left==z:
                y.parent.left=y
            else:
                y.parent.right=y
        z.height=1+max(self.get_height(z.left),self.get_height(z.right))
        y.height=1+max(self.get_height(y.left),self.get_height(y.right))


def find_min(r):
    while r.left:
        r = r.left
    return r

def find_max(r):
    while r.right:
        r = r.right
    return r




a = [13,10,8,11,14,7,6]
b = [2,4,1,3]
tree = AVL()
for i in a:
    tree.insert(i)

tree.print()
print(tree.getBalance())





