class stackList:
    def __init__(self):
        self.list = []

    def push(self, value):
        self.list.append(value)
        return "Value inserted"

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0

    def deleteStack(self):
        self.list = []
        return "Stack deleted"

    def peek(self):
        return self.list[-1]


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class stackLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return newNode

    def pop(self):
        if self.length == 0:
            raise Exception('stack is empty')
        if self.length == 1:
            currentNode = self.head
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            currentNode = current.next
            current.next = None
            self.tail = current
        self.length -= 1
        return currentNode.value

    def isEmpty(self):
        return self.length == 0

    def deleteStack(self):
        self.head = None
        self.tail = None
        self.length = 0
        return "Stack deleted"

    def peek(self):
        return self.tail.value

    def __str__(self):
        temp = self.head
        total = ''
        while temp:
            total += f"{temp.value}"
            temp = temp.next
            
            if temp is not None:
                total += '\n'
        
        return total

common = Node(2)
common.next = Node(3)

head1 = Node(33)
head1.next = Node(7)
head1.next.next = common

head2 = Node(22)
head2.next = Node(8)
head2.next.next = common


def printList(head:Node):
    while head:
        print(head.value , end=' -> ')
        head = head.next
    print('None')
    
print('List1')
printList(head1)
print('List2')
printList(head2)

def getIntersectionNode(List1:Node,List2:Node):
    visited = set()
    while List1:
        visited.add(List1)
        List1 = List1.next
    while List2:
        if List2 in visited:
            return List2
        List2 = List2.next
    return None

intersection = getIntersectionNode(head1,head2)
if intersection:
    print(f"Intersection at node with value : {intersection.value}")
else:
    print(f"No intersection")
    
class ThreeStack:
    def __init__(self,stackSize):
        self.numberOfStack = 3
        self.stackSize = stackSize
        self.stack = [None] * (stackSize * self.numberOfStack)
        self.sizes = [-1] * self.numberOfStack
        
    def getIndex(self,stackNum):
        return (stackNum * self.numberOfStack) + self.sizes[stackNum]
    
    def push(self,stackNum,value):
        if self.sizes[stackNum] + 1 >= self.stackSize:
            return 'Stack is full'
        
        self.stack[self.getIndex(stackNum)] = value
        self.sizes[stackNum] += 1
        
    def pop(self,stackNum):
        if self.sizes[stackNum] == -1:
            return 'Stack is empty'
        deletedValue = self.stack[self.getIndex(stackNum)]
        self.stack[self.getIndex(stackNum)] = None
        self.sizes[stackNum] -= 1
        return deletedValue
    
    def peek(self,stackNum):
        if self.sizes[stackNum] == -1:
            return None
        return self.stack(self.getIndex(stackNum))
        
        
# def deleteNode(rootNode, nodeValue):
#     if rootNode is None:
#         return rootNode
#     if nodeValue < rootNode.data:
#         rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
#     elif nodeValue > rootNode.data:
#         rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
#     else:
#         if rootNode.leftChild is None:
#             temp = rootNode.rightChild
#             rootNode = None
#             return temp
        
#         if rootNode.rightChild is None:
#             temp = rootNode.leftChild
#             rootNode = None
#             return temp
        
#         temp = minValueNode(rootNode.rightChild)
#         rootNode.data = temp.data 
#         rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
#     return rootNode