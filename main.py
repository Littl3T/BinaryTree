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
    else:
        root.left = insert(root.left, key)
    root = balance_tree(root)
    return root

def insert_values(root, values):
    for value in values:
        root = insert(root, value)
    return root

def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1

def balance(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)

def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    return y

def balance_tree(node):
    if not node:
        return None
    
    bal = balance(node)
    
    if bal > 1:
        if balance(node.left) < 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)
    
    if bal < -1:
        if balance(node.right) > 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)
    
    return node

def print2DTree(root, space=0, LEVEL_SPACE=5):
    if root is None:
        return
    space += LEVEL_SPACE
    print2DTree(root.right, space)
    for i in range(LEVEL_SPACE, space):
        print(end=" ")
    print("|" + str(root.value) + "|<")
    print2DTree(root.left, space)

# Test the implementation
root = insert_values(None, [10,11,6,4,3,5])
print("-" * 10)
print("Balance of the root: ", balance(root))
print2DTree(root)