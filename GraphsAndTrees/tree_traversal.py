class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(f' {root.data} ')
    inorder(root.right)

def preorder(root):
    if root is None:
        return
    print(f' {root.data} ')
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(f' {root.data} ')


def createTree():
    # Constructing the below tree
    #         5 
    #        / \ 
    #      3     6 
    #     / \     \ 
    #     1  4     8 
    #    / \      / \ 
    #    0 2      7  9

    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.right.right = Node(8)
    root.left.left.left = Node(0)
    root.left.left.right = Node(2)
    root.right.right.left = Node(7)
    root.right.right.right = Node(9)
    return root

if __name__ == "__main__":
    root = createTree()
    inorder(root)
    preorder(root)
    postorder(root)