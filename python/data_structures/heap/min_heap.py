# data_structures/heap/min_heap.py
class MinHeap:
    def __init__(self):
        self._data = []
    
    def _parent(self, i):
        return (i -1) // 2
    
    def _left(self, i):
        return (2 * i) + 1
    
    def _right(self, i):
        return (2 * i) + 2
    
    def insert(self, value):
        self._data.append(value)
        self.heapify_up(len(self._data) - 1)
    
    def pop(self):
        if not self._data:
            raise IndexError("Heap empty")

        if len(self._data) == 1:
            return self._data.pop()

        root = self._data[0]
        self._data[0] = self._data.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self,i):
        smallest = i 
        left = self._left(i) 
        right = self._right(i)

        if left < len(self._data) and self._data[left] < self._data[smallest]:
            smallest = left 
        if right < len(self._data) and self._data[right] < self._data[smallest]:
            smallest = right
        
        if smallest != i:
            self._heapify_down(smallest)
        if smallest != i:
            self._data[i], self._data[smallest] = self._data[smallest], self._data[i]
            self._heapify_down(smallest)

    def heapify_up(self, i):

        while(i > 0 and self._data[i] < self._data[self._parent(i)]):
            p = self._parent(i)
            self._data[i], self._data[p] = self._data[p],self._data[i]
            i = p
