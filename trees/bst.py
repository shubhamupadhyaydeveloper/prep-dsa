from collections import deque


class Bst:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


def preOrder(tree: Bst):
    if not tree:
        return None

    print(tree.value)
    preOrder(tree.leftChild)
    preOrder(tree.rightChild)


def inOrder(tree: Bst):
    if not tree:
        return None

    inOrder(tree.leftChild)
    print(tree.value)
    inOrder(tree.rightChild)


def postOrder(tree: Bst):
    if not tree:
        return None

    postOrder(tree.leftChild)
    postOrder(tree.rightChild)
    print(tree.value)


def levelOrder(tree: Bst):
    if not tree:
        return None

    queue = deque([tree])
    while queue:
        current = queue.popleft()
        print(current.value)

        if current.leftChild:
            queue.append(current.leftChild)

        if current.rightChild:
            queue.append(current.rightChild)


def searchValue(tree: Bst, value):
    if not tree:
        return None

    if tree.value == value:
        return True

    if tree.value >= value:
        return searchValue(tree.leftChild, value)

    if tree.value < value:
        return searchValue(tree.rightChild, value)

    return False


def insertValue(tree: Bst, value):
    if not tree:
        return None

    newNode = Bst(value)

    if tree.value > value:
        if tree.leftChild:
            insertValue(tree.leftChild, value)
        else:
            tree.leftChild = newNode
            return "Node Inserted"

    if tree.value < value:
        if tree.rightChild:
            insertValue(tree.rightChild, value)
        else:
            tree.rightChild = newNode
            return "Node Inserted"


def minNodeValue(tree: Bst):
    current = tree
    while tree.leftChild is not None:
        current = current.leftChild

    return current


def deleteNode(tree: Bst, value):
    if not tree:
        return None

    if tree.value > value:
        tree.leftChild = deleteNode(tree.leftChild, value)

    elif tree.value < value:
        tree.rightChild = deleteNode(tree.rightChild, value)

    else:
        minValue = minNodeValue(tree.rightChild)
        tree.value = minValue.value
        deleteNode(tree, minValue)
        return
    
def deleteBst(tree:Bst):
    if not tree:
        return
    
    tree.value = None
    tree.rightChild = None
    tree.leftChild = None
