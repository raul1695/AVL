"""

This is my implementation of the AVL tree. 


"""



class TreeNode:
    def __init__(self, key = None):
        self.val = key
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)


class AVL:
    def __init__(self, key = None):
        self.root = TreeNode(key)

    def insert(self,key):
        print("Attempting to add value ... " + str(key))
        temp = None  #temporarily holds the parent node
        itr = self.root

        if(itr.val == None):
            self.root.val = key
            return
        print("We are here")
        while itr:
            print("print going through loop")
            temp = itr
            if(itr.val > key):
                print("print going through 1")
                itr = itr.left
            elif(itr.val < key):
                print("print going through 2")
                itr = itr.right
            elif(itr.val == key):
                print("print going through 3")
                return

        if(temp.val > key):
            temp.left = TreeNode(key)
            return
        else:
            temp.right = TreeNode(key)

    def height_recursive(self,node):
        if(node == None):
            return -1
            
        return max(self.height_recursive(node.left) ,self.height_recursive(node.right)) +1

    def getBalanceFactor(self,node):
        l = self.height_recursive(node.left)
        r = self.height_recursive(node.right)

        return l - r

    def getBalance(self):
        return self.getBalanceFactor(self.root)

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


        

def find_min(r):
    while r.left:
        r = r.left
    return r

def find_max(r):
    while r.right:
        r = r.right
    return r




a = [13,10,8,11,14]
b = [2,4,1,3]
tree = AVL()
for i in a:
    tree.insert(i)

tree.print()
print(tree.getBalance())





