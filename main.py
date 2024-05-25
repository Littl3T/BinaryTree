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
    root = balance_tree(root)
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

def rotate_right(node):
    A = node
    B = node.left
    t = B.right
    B.right = A
    A.left = t
    return B

def rotate_left(node):
    A = node
    B = node.right
    t = B.left
    B.left = A
    A.right = t
    return B

def balance_tree(root:object):
    if balance(root) >1:
        if balance(root.left) >1 or balance(root.left) <-1:
            balance_tree(root.left)
        else:
            root = rotate_right(root)
    if balance(root) <-1:
        if balance(root.right) >1 or balance(root.right) <-1:
            balance_tree(root.right)
        else:
            root = rotate_left(root)
    return root
    

def print2DTree(root, space=0, LEVEL_SPACE = 5):
    if (root == None): return
    space += LEVEL_SPACE
    print2DTree(root.right, space)
    # print() # neighbor space
    for i in range(LEVEL_SPACE, space): print(end = " ")  
    print("|" + str(root.value) + "|<")
    print2DTree(root.left, space)


root = insert_values(None, [0,1,2,3,4,5,6,7,8,9,10,11])
print("-"*10)
print("Balance of the root: ", balance(root))
print2DTree(root)