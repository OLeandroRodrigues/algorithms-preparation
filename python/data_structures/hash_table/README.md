# 📝 Hash Table Proof

## 📚 Metadata

- **Creator / Inventor:** Origin traced to mid-20th century computer science  
- **Country of Origin:** United States (early work by IBM researchers)  
- **Institution (if applicable):** Concept formalized in early algorithmic research (1950s)  
- **Year of Creation / Publication:** First formal description around 1953–1954  
- **Primary Reference:** *The Art of Computer Programming* — Donald E. Knuth  
- **Related Concepts:** Buckets, Hash Function, Compression Function, Collisions, Separate Chaining, Open Addressing, Load Factor, Rehashing  
- **Typical Use Cases:** Dictionaries, symbol tables, caches, sets, associative arrays, compilers, interpreters, database indexing, routing tables  

---

## 📝 Description

A **Hash Table** is a data structure that provides **average O(1)** time for insertion, search, and deletion, using a **hash function** to map keys to array indices.

At a high level, the structure looks like this:

```
index:   0      1      2      3      4
         ↓      ↓      ↓      ↓      ↓
       [ - ]  [ A ]  [ - ]  [ B ]  [ C ]
                 ↓            ↓      ↓
               [ D ]        [ E ]  [ F ]
```

Typical components:

### **Hash Function**
Converts a key of arbitrary type into an integer (raw hash).

### **Compression Function**
Maps the hash into an array index:

```
index = hash(key) mod capacity
```

### **Collision Resolution Strategy**
When two keys map to the same index:

- **Separate Chaining**: Use a linked list for each bucket  

### **Load Factor (α)**

```
α = size / capacity
```

When α exceeds a threshold (typically **0.75**), the table must **rehash**.

### **Rehashing**
- Create a new table with doubled capacity  
- Re-insert all existing elements  
- Ensures performance remains O(1) on average  

---

## 📝 Pseudocode (Separate Chaining)

```cpp
STRUCT Node:
    key
    value
    next

STRUCT HashTable:
    buckets[]   // array of Node*
    size
    capacity
    load_threshold = 0.75

INIT(T, initial_capacity):
1  T.capacity = initial_capacity
2  T.buckets = array of size initial_capacity filled with null
3  T.size = 0

HASH(key):
1  raw = key.hashCode()
2  raw = raw & 0x7FFFFFFF        // remove sign bit
3  return raw

INDEX(T, key):
1  return HASH(key) mod T.capacity

PUT(T, key, value):
1  if LOAD_FACTOR(T) >= load_threshold:
2      REHASH(T)
3
4  idx = INDEX(T, key)
5  node = T.buckets[idx]
6  
7  while node != null:
8      if node.key == key:
9          node.value = value
10         return
11     node = node.next
12
13 newNode = new Node(key, value)
14 newNode.next = T.buckets[idx]
15 T.buckets[idx] = newNode
16 T.size++

GET(T, key):
1  idx = INDEX(T, key)
2  node = T.buckets[idx]
3  while node != null:
4      if node.key == key:
5          return node.value
6      node = node.next
7  error "key not found"

CONTAINS_KEY(T, key):
1  idx = INDEX(T, key)
2  node = T.buckets[idx]
3  while node != null:
4      if node.key == key:
5          return true
6      node = node.next
7  return false

REMOVE(T, key):
1  idx = INDEX(T, key)
2  prev = null
3  node = T.buckets[idx]
4  while node != null:
5      if node.key == key:
6          if prev == null:
7              T.buckets[idx] = node.next
8          else:
9              prev.next = node.next
10         T.size--
11         return true
12     prev = node
13     node = node.next
14 return false

LOAD_FACTOR(T):
1  return T.size / T.capacity

REHASH(T):
1  oldBuckets = T.buckets
2  T.capacity = T.capacity * 2
3  T.buckets = new array of size T.capacity
4  T.size = 0
5  
6  for each bucket in oldBuckets:
7      node = bucket
8      while node != null:
9          PUT(T, node.key, node.value)
10         node = node.next
```

---

## 1. Invariant

At any moment:

- Bucket structure, hash mapping, collision integrity, uniqueness, and load factor safety are preserved.

---

## 2. Correctness

All operations (`PUT`, `GET`, `REMOVE`, `CONTAINS_KEY`, `REHASH`) correctly preserve structure and invariants.

---

## 3. Termination

All loops operate on finite lists and always terminate.

---

## 4. Time Complexity

Average:
- PUT: O(1)
- GET: O(1)
- REMOVE: O(1)

Worst case: O(n)

Rehash: amortized O(1)

---

## 5. Space Complexity

```
O(n + m)
```

---

## 6. Additional Notes

Performance depends on hash function quality and collision strategy.

---

## 7. Handwritten Draft (optional)

(Insert your notes here.)
