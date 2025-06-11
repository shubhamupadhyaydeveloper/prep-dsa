class Heap:
    def __init__(self, size):
        self.heapSize = 0
        self.list = [None] * (size + 1)
        self.maxSize = size + 1

    def peek(self):
        return self.list[1]

    def sizeOfHeap(self):
        return self.maxSize

    def levelOrder(self):
        for node in range(1, len(self.list)):
            print("this is node", node)

    def heapifyInsert(self, index, heapType):
        if index <= 1:
            return

        parentIndex = index // 2

        if heapType == "Min":
            if self.list[parentIndex] > self.list[index]:
                self.list[parentIndex], self.list[index] = self.list[index], self.list(
                    parentIndex
                )
                self.heapifyInsert(parentIndex, heapType)
        else:
            if self.list[parentIndex] < self.list[index]:
                self.list[parentIndex], self.list[index] = self.list[index], self.list(
                    parentIndex
                )
                self.heapifyInsert(parentIndex, heapType)

    def insertValue(self, value, heapType):
        if self.heapSize + 1 == self.maxSize:
            return "Heap is full"

        self.list[self.heapSize + 1] = value
        self.heapSize += 1

        self.heapifyInsert(len(self.list), heapType)
        return "Value is inserted"

    def heapifyRemove(self, index, heapType):
        leftIndex = index * 2
        rightIndex = index * 2 + 1
        swapChild = 0

        if self.heapSize < index:
            return

        elif self.heapSize == index:
            if heapType == "Max":
                if self.list[leftIndex] > self.list[index]:
                    self.list[leftIndex], self.list[index] = (
                        self.list[index],
                        self.list[leftIndex],
                    )
                return
            else:
                if self.list[leftIndex] > self.list[index]:
                    self.list[leftIndex], self.list[index] = (
                        self.list[index],
                        self.list[leftIndex],
                    )
                return

        else:
            if heapType == "Max":
                if self.list[leftIndex] > self.list[rightIndex]:
                    swapChild = leftIndex
                else:
                    swapChild = rightIndex

                if self.list[swapChild] > self.list[index]:
                    self.list[swapChild], self.list[index] = (
                        self.list[index],
                        self.list[swapChild],
                    )
            else:
                if self.list[leftIndex] < self.list[rightIndex]:
                    swapChild = leftIndex
                else:
                    swapChild = rightIndex

                if self.list[swapChild] < self.list[index]:
                    self.list[swapChild], self.list[index] = (
                        self.list[index],
                        self.list[swapChild],
                    )

        self.heapifyRemove(swapChild, heapType)

    def removeValue(self, heapType):
        if self.heapSize == 0:
            return None

        lastNode = self.list[self.heapSize]
        self.list[self.heapSize] = None
        self.list[1] = lastNode

        self.heapSize -= 1

        self.heapifyRemove(1, heapType)
