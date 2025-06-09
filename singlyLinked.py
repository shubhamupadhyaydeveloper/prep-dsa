class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return "Value inserted at start"

    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return "Value inserted at end"

    def removeFirst(self):
        if self.length == 0:
            return "List empty"
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return "removed successfully"
        nodeToBeRemoved = self.head
        newNode = self.head.next

        self.head = newNode
        nodeToBeRemoved.next = None

        self.length -= 1
        return "removed successfully"

    def removeLast(self):
        if self.length == 0:
            return "List empty"
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return "removed successfully"
        newLastNode = self.head
        while newLastNode.next.next:
            newLastNode = newLastNode.next
        newLastNode.next = None
        self.tail = newLastNode
        self.length -= 1
        return "removed successfully"

    def remove(self, index):
        if index >= self.length or index < 0:
            return Exception("invalid index")

        if index == 0:
            return self.removeFirst()

        if index == self.length - 1:
            return self.removeLast()

        currentNode = self.head
        for _ in range(index - 1):
            currentNode = currentNode.next

        nodeToBeRemoved = currentNode.next
        currentNode.next = nodeToBeRemoved.next
        nodeToBeRemoved.next = None
        self.length -= 1
        return "removed successfully"

    def __str__(self):
        current = self.head
        display = []
        while current:
            if current.next:
                display.append(f"{current.data} ->")
            else:
                display.append(f"{current.data}")
            current = current.next
        return " ".join(display)

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def getMiddle(self):
        middle = self.length // 2
        current = self.head
        for _ in range(middle):
            current = current.next
        return current.data

    def getItem(self, index):
        if index > self.length or index < 0:
            return Exception("invalid index")

        current = self.head
        for _ in range(index):
            current = current.next

        return current

    def isDuplicate(self):
        visited = set()
        current = self.head
        index = 0
        while current:
            if current.data in visited:
                self.remove(index)
                current = self.getItem(index).next
            else:
                visited.add(current.data)
                current = current.next
                index += 1
    
    def removeParticlarDuplicateNode(self,value):
        index = 0
        current = self.head
        while current:
            if current.data == value:
                self.remove(index)
                current = self.getItem(index).next
            else:
                current = current.next
                index += 1
    
    def isPalindrome(self):
        start = self.head
        check = ''
        while start:
            check += f"{start.data}"
            start = start.next
        rev = check[::-1]
        if rev == check:
            return True
        return False

def mergeList(list1:LinkedList,list2:LinkedList):
    node1 = list1.head
    node2 = list2.head
    sortedList = LinkedList()
    
    while node1 and node2:
        if node1.data >= node2.data:
            sortedList.append(node2.data)
            node2 = node2.next
        else:
            sortedList.append(node1.data)
            node1 = node1.next
            
    while node1:
        sortedList.append(node1.data)
        node1 = node1.next
        
    while node2:
        sortedList.append(node2.data)
        node2 = node2.next
        
    return sortedList
                           
                
# myWay               
# def mergeList(list1:LinkedList,list2:LinkedList):
#     i = j = 0
#     sortedList = LinkedList()
#     while i < list1.length and j < list2.length:
#         if list1.getItem(i).data > list2.getItem(j).data:
#             sortedList.append(list2.getItem(j).data)
#             j += 1
#         else:
#             sortedList.append(list1.getItem(i).data)
#             i += 1
    
#     while i < list1.length:
#         sortedList.append(list1.getItem(i).data)
#         i += 1
        
#     while j < list2.length:
#         sortedList.append(list2.getItem(j).data)
#         j += 1
        
#     return sortedList
    

# filepath: /Volumes/External2/dsaprep/singlyLinked.py
# This is my way
# def reverseList(linkedList: LinkedList):
#     reverseList = LinkedList()
#     current = linkedList.head
#     while current:
#         reverseList.prepend(current.data)
#         current = current.next
#     return reverseList


myList = LinkedList()
myList.append(1)
myList.append(2)
# myList.append(2)
# myList.append(1)
# myList2 = LinkedList()
# myList2.append(4)
# myList2.append(5)
# myList2.append(5)
# myList2.append(6)
# myList2.append(7)
# myList2.append(8)
# myList2.append(8)
# myList.append(7)
# print(myList.getMiddle())
# print(myList)
# myList.isDuplicate()
# print(myList)
# print('list1',myList)
# print('list2',myList2)
# print(mergeList(myList,myList2))
print(myList)
print(myList.isPalindrome())

