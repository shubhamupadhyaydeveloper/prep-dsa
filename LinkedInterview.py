from random import randint


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return " -> ".join(values)

    def __len__(self):
        return self.length

    def add(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self.tail

    def pop_first(self):
        if self.length == 1:
            self.head = None
            self.tail = None

        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        self.length -= 1
        return popped_node.value

    def pop(self):
        if self.length == 1:
            self.tail = None
            self.head = None
        elif self.length == 0:
            return
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
            self.tail = current
        self.length -= 1
        return True

    def remove(self, index: int):
        current = self.head
        if index == 0:
            second_value = current.next
            self.head = second_value
            current.next = None
            return current.value
        elif index == self.length - 1:
            return self.pop()
        elif index < 0 or index > self.length:
            raise IndexError("Invalid Index out of range")
        else:
            for _ in range(index - 1):
                current = current.next

            popped_node = current.next
            current.next = popped_node.next
            popped_node.next = None
        self.length -= 1
        return True

    def generate(self, minValue, maxValue):
        newList = LinkedList()
        for _ in self:
            newList.add(randint(minValue, maxValue))
        return newList

    def removeDuplicate(self):
        visited = set()
        if self.length == 0 or self.length == 1:
            return True
        current = self.head
        index = 0
        while current:
            if current.value in visited:
                nextItem = current.next
                self.remove(index)
                current = nextItem
            else:
                visited.add(current.value)
                current = current.next
                index += 1

    def elementFromLast(self, index):
        if index >= len(self) or index < 0:
            raise Exception("invalid index")
        lastIndex = len(self) - index - 1
        print("this is lenght", lastIndex)
        current = self.head
        for _ in range(lastIndex):
            current = current.next

        return current.value

    def partition(self, value):
        leftValues = LinkedList()
        rightValues = LinkedList()

        for node in self:
            if node.value >= value:
                rightValues.add(node.value)
            else:
                leftValues.add(node.value)

        return leftValues, rightValues

    def inPlacePartition(self, value):
        current = self.head
        self.tail = self.head

        while current:
            nextNode = current.next
            current.next = None

            if current.value >= value:
                current.next = self.head
                self.head = current
            else:
                self.tail.next = current
                self.tail = current

            current = nextNode

        if self.tail.next is not None:
            self.tail.next = None


def sumTwoList(list1: LinkedList, list2: LinkedList):
    if len(list1) < 0 and len(list2) < 0:
        raise Exception("both lists are empty")

    firstListSum = ""
    secondListSum = ""

    for node in list1:
        firstListSum += str(node.value)

    for node in list2:
        secondListSum += str(node.value)

    newValue = str(int(firstListSum[::-1]) + int(secondListSum[::-1]))

    newList = LinkedList()

    for value in newValue[::-1]:
        newList.add(value)
        
    return newList  




myList = LinkedList()
myList.add(4)
myList.add(2)
myList.add(3)
myList.add(5)
mySecondList = LinkedList()
mySecondList.add(6)
mySecondList.add(8)
mySecondList.add(7)
mySecondList.add(9)
print(myList)
print(mySecondList)
print(sumTwoList(myList, mySecondList))
