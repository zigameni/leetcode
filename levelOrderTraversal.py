
# Node structure
class Node:
    # creating new Node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Function to print level order traversal of tree


def printLevelOrder(root):
    h = height(root)
    for i in range(h+1):
        printCurrentLevel(root, i)


# print nodes at current level
def printCurrentLevel(root, level):
    if(root is None):
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)


def height(node):
    if node is None:
        return 0
    else:
        # compute height of sub tree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if(lheight > rheight):
            return lheight+1
        else:
            return rheight+1


# Driver program
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is -")
printLevelOrder(root)
