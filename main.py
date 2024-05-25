class bst:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
def insert(root, key):
    if not root:
        return bst(key)
    if key >= root.value:
        root.right = insert(root.right, key)
    elif key < root.value:
        root.left = insert(root.left, key)
    return root

def insert_values(root, values):
    for value in values:
        root = insert(root, value)
    return root

def height(node:object):
    H = 0
    R = node.right
    L = node.left
    
    if R!= None and L!= None:
        H = max(height(L), height(R)) +1
    elif R!= None and L == None:
        H = height(R) + 1
    elif R == None and L != None:
        H = height(L) +1
    return H

def balance(node):
    R = node.right
    L = node.left
    if R!= None and L!= None:
        B = height(L) - height(R)
    elif R!= None and L == None:
        B = -1 -height(R)
    elif R == None and L != None:
        B = height(L) + 1
    return B


def print2DTree(root, space=0, LEVEL_SPACE = 5):
    if (root == None): return
    space += LEVEL_SPACE
    print2DTree(root.right, space)
    # print() # neighbor space
    for i in range(LEVEL_SPACE, space): print(end = " ")  
    print("|" + str(root.value) + "|<")
    print2DTree(root.left, space)


root = insert_values(None, [2,1,3])
print2DTree(root) 

print(height(root))
print(balance(root))