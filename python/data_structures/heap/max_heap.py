
class MaxHeap:
    def __init__(self):
        self._data = [] 
        
    def _parent(self, i):
        return (i - 1) // 2
    
    def _left(self, i):
        return i * 2 + 1
    
    def _right(self, i):
        return i * 2 + 2
    
    def insert(self,value):
        self._data.append(value)
        self._heapify_up(len(self._data) - 1)
    
    def pop(self):
        if not self._data:
            raise IndexError('Heap empty')

        if len(self._data) == 1:
            return self._data.pop()
        
        root = self._data[0]

        self._data[0] = self._data.pop()
        self._heapify_down(0)
        return root


    def _heapify_up(self, i):
        while i > 0 and self._data[i] > self._data[self._parent(i)]:
            p = self._parent(i)
            self._data[i], self._data[p] = self._data[p], self._data[i]
            i = p
        
    def _heapify_down(self, i):
        biggest = i
        left = self._left(i)
        right = self._right(i)

        if left < len(self._data) and self._data[left] > self._data[biggest]:
            biggest = left
        if right < len(self._data) and self._data[right] > self._data[biggest]:
            biggest = right
        
        if biggest != i: 
            self._data[i], self._data[biggest] = self._data[biggest], self._data[i]
            self._heapify_down(biggest)



           