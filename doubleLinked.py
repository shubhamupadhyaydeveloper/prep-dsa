class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            self.tail.next = newNode
            newNode.next = self.head
            self.tail = newNode
        self.length += 1
        return "node Inserted"

    def removeFirst(self):
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        nodeToBeRemoved = self.head
        newNode = self.head.next

        self.head = newNode
        nodeToBeRemoved.next = None
        self.length -= 1
        return "node removed"

    def removeLast(self):
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        nodeToBeRemoved = self.tail
        newNode = self.head
        while newNode.next.next:
            newNode = newNode.next
        newNode.next = nodeToBeRemoved.next
        nodeToBeRemoved.next = None
        self.length -= 1
        return "node removed"

    def remove(self, index):
        if index > self.length or index < 0:
            return Exception("invalid index")

        if index == 0:
            self.removeFirst()
            return "node Removed"

        if index == self.length - 1:
            self.removeLast()
            return "node Removed"

        current = self.head
        for _ in range(index - 1):
            current = current.next
        currentItem = current.next
        current.next = current.next.next
        currentItem.next = None
        self.length -= 1
        return "node removed"

    def countNodes(self):
        number = 0
        current = self.head
        while current:
            number += 1
            current = current.next
        return number

    def splitList(self):
        if self.length == 0:
            return None, None
        firstList = LinkedList()
        secondList = LinkedList()
        midIndex = None
        if self.length % 2 == 0:
            midIndex = self.length // 2
        else:
            midIndex = (self.length // 2) + 1
        current = self.head
        for _ in range(midIndex):
            firstList.append(current.data)
            current = current.next

        for _ in range(midIndex, self.length):
            secondList.append(current.data)
            current = current.next

        return f"firstList {firstList} secondList {secondList}"

    def isSorted(self):
        if self.head is None or self.head.next == self.head:
            return True

        current = self.head
        while current and current.next:
            if current.next == self.head:
                break
            if current.data > current.next.data:
                return False
            current = current.next

        return True

    def insertIntoSorted(self, value):
        newNode = Node(value)
        current = self.head
        
        if self.head is None:
            self.append(value)
            return 'node Inserted'
        
        if value < self.head.data:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
            self.length += 1
            return 'node inserted'
            
        while (current.next != self.head and current.next.data < value):
            current = current.next
            
        newNode.next = current.next
        current.next = newNode
        
        if current == self.tail:
            self.tail = current
        
        return 'Node Inserted'
        

    def __str__(self):
        if not self.head:
            return "Empty List"

        display = []
        current = self.head
        while True:
            display.append(f"{current.data}")
            current = current.next
            if current == self.head:
                break
            else:
                display.append(" -> ")
        return "".join(display)


myList = LinkedList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.append(5)
# print(myList.countNodes())
print(myList)
print(myList.insertIntoSorted(0))
print(myList)
# print(myList.isSorted())
# print(myList.splitList())
