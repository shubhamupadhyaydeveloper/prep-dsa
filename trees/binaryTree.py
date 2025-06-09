from collections import deque


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.rightChild = None
        self.leftChild = None


def preOrder(tree: BinaryTree):
    if not tree:
        return None

    print(tree.value)
    preOrder(tree.leftChild)
    preOrder(tree.rightChild)


def inOrder(tree: BinaryTree):
    if not tree:
        return None

    inOrder(tree.leftChild)
    print(tree.value)
    inOrder(tree.rightChild)


def postOrder(tree: BinaryTree):
    if not tree:
        return None

    postOrder(tree.leftChild)
    postOrder(tree.rightChild)
    print(tree.value)


def levelOrder(tree: BinaryTree):
    if not tree:
        return None

    queue = deque([])
    queue.append(tree)

    while queue:
        currentNode: BinaryTree = queue.popleft()
        print(f"Node {currentNode.value}")

        if currentNode.leftChild is not None:
            queue.append(currentNode.leftChild)

        if currentNode.rightChild is not None:
            queue.append(currentNode.rightChild)


def searchValue(tree: BinaryTree, value):
    if not tree:
        return

    queue = deque([])
    queue.append(tree)

    while queue:
        currentNode: BinaryTree = queue.popleft()

        if currentNode.value == value:
            return True

        if currentNode.leftChild is not None:
            queue.append(currentNode.leftChild)

        if currentNode.rightChild is not None:
            queue.append(currentNode.rightChild)

    return False


def insertNode(tree: BinaryTree, value):
    if not tree:
        return None

    newNode = BinaryTree(value)
    queue = deque([])
    queue.append(tree)

    while queue:
        currentNode: BinaryTree = queue.popleft()

        if currentNode.leftChild:
            queue.append(currentNode.leftChild)
        else:
            currentNode.leftChild = newNode
            return "Node Inserted"

        if currentNode.rightChild:
            queue.append(currentNode.rightChild)
        else:
            currentNode.rightChild = newNode
            return "Node Inserted"


def findDeepestNode(tree: BinaryTree):
    if not tree:
        return None

    queue = deque([])
    queue.append(tree)

    currentNode = None
    while queue:
        currentNode = queue.popleft()

        if currentNode.leftChild is not None:
            queue.append(currentNode.leftChild)

        if currentNode.rightChild is not None:
            queue.append(currentNode.rightChild)

    return currentNode


def deleteLastNode(tree: BinaryTree):
    if not tree:
        return None
    
    if not tree.leftChild and not tree.rightChild:
        return None

    queue = deque([tree])
    lastParent = None
    isLeftChild = False

    while queue:
        currentNode = queue.popleft()

        if currentNode.leftChild is not None:
            lastParent = currentNode
            queue.append(currentNode.leftChild)
            isLeftChild = True

        if currentNode.rightChild is not None:
            lastParent = currentNode
            queue.append(currentNode.rightChild)
            isLeftChild = False
    
    
    if lastParent:
        if isLeftChild:
            lastParent.leftChild = None
        else:
            lastParent.rightChild = None
            
    return tree

def deleteNode(tree:BinaryTree,value):
    if not tree:
        return None
    
    queue = deque([tree])
    
    while queue:
        current = queue.popleft()
        if current.value == value:
            lastNodeValue = findDeepestNode(tree)
            current.value = lastNodeValue.value
            deleteLastNode(tree)
            return 'Node Deleted'
        
        if current.leftChild is not None:
            queue.append(current.leftChild)

        if current.rightChild is not None:
            queue.append(current.rightChild)
            
    return tree

def deleteBst(tree:BinaryTree):
    if not tree:
        return None
    
    tree.value = None
    tree.leftChild = None
    tree.rightChild = None
    
        


node = BinaryTree("Drinks")
nodeLeftChild = BinaryTree("Hot")
nodeRightChild = BinaryTree("Cold")

hotLeftChild = BinaryTree("Coffee")
hotRightChild = BinaryTree("Tea")

coldLeftChild = BinaryTree("Icecream")
coldRightChild = BinaryTree("ColdCoffee")

node.leftChild = nodeLeftChild
node.rightChild = nodeRightChild

nodeLeftChild.leftChild = hotLeftChild
nodeLeftChild.rightChild = hotRightChild

nodeRightChild.leftChild = coldLeftChild
nodeRightChild.rightChild = coldRightChild
