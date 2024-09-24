class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def insert_avl(node, key):
    if not node:
        return AVLNode(key)
    
    if key < node.key:
        node.left = insert_avl(node.left, key)
    else:
        node.right = insert_avl(node.right, key)

    node.height = 1 + max(get_height(node.left), get_height(node.right))

    balance = get_balance(node)

    if balance > 1 and key < node.left.key:
        return right_rotate(node)

    if balance < -1 and key > node.right.key:
        return left_rotate(node)

    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

def inorder_avl(root):
    if root:
        inorder_avl(root.left)
        print(root.key, end=' ')
        inorder_avl(root.right)

root = None
root = insert_avl(root, 10)
root = insert_avl(root, 20)
root = insert_avl(root, 30)
root = insert_avl(root, 40)
root = insert_avl(root, 50)
root = insert_avl(root, 25)

inorder_avl(root)  # 出力: 10 20 25 30 40 50
