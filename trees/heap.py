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
        if self.heapSize == self.maxSize:
            return "Heap is full"

        self.list[len(self.list)] = value
        self.heapSize += 1

        self.heapifyInsert(len(self.list), heapType)
