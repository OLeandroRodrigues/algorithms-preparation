# 📝 Priority Queue Proof

## 📚 Metadata
- **Creator / Inventor**: Origin uncertain
- **Country of Origin**: N/A
- **Institution (if applicable)**: N/A 
- **Year of Creation / Publication**: Method known since 1964. 

## 📝 Description
A 'priority queue' is a data structure for maintaining a set S of elements, each
with an associated value called a key. Similar to a regular queue, but with an important difference:
    In a regular queue: elements leave in the order they entered (FIFO — first in, first out).
    In a priority queue: each element has an associated priority (key), and the element with the highest priority (key) is always served (removed) first, regardless of the order of arrival


## 📝 Pseudocode
cpp
```
MAX-HEAP-MAXIMUM(A)
1 if A.heap-size < 1
2    error "heap underflow"
3 return A[1]

MAX-HEAP-EXTRACT-MAX(A)
1 max = MAX-HEAP-MAXIMUM(A)
2 A[1] = A[A.heap-size]
3 A.heap-size = A.heap-size - 1
4 MAX-HEAPIFY(A,1)
5 return max


MAX-HEAP-INCREASE-KEY(A,x,k)
1 if k < x.key
2    error "new key is smaller than current key"
3 x.key = k
4 find the index i in an array A where object x ocurrs
5 while i > 1 and A[PARENT(i)].key < A[i].key
6    exchange A[i] with A[PARENT(i)], updating the information that
     maps priority queue objetcs to array indices
7    i = PARENT(i)

MAX-HEAP-INSERT(A,x,n)
1 if A.heap-size < n
2   error "heap overflow"
3 A.heap-size = A.heap-size + 1
4 k = x.key
5 x.key = - infinity
6 A[A.heap-size] = x
7 map x to index heap-size in the array
8 MAX-HEAP-INCREASE-KEY(A,x,k)
```

## ✅ Proof Checklist

The priority queue is implemented through a heap, so the operations are all similar to the heap, except for the overhead caused by the need to map an array item to a queue object, 

To analyze the Invariant, Correctness, Termination, Time Complexity: [Heap Data Structure](../heap/README.md)  

---

## 1. Additional Notes


- It can be implemented as a min-priority-queue or a max-priority-queue. There are two ways to implement the queue: the standard form, where it is not possible to guarantee the execution order of items with the same priority — that is, for 3 items with the same priority, it is not possible to know which one will be executed first; the last item that just entered may be executed first or last. And the stable type, which guarantees the order; this type is made possible through a new attribute in the priority queue object defined as a timestamp

- If a priority queue only requires push and pop operations, it is not necessary to implement it using a HashTable. But if there are other operations, a HashTable becomes essential; although there is some overhead, there is a gain in performance

---
