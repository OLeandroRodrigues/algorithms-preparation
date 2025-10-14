"""
Problem: Find the k largest elements in an array.

Approach:
  - From Scratch: implement a max-heap of size k.

Complexity:
  - Time: O(n log k)
  - Space: O(k)
"""
    
data = []
  
def insert(value):
      data.append(value)
      heapify_up(len(data) - 1)

def pop():
  if len(data) == 1:
    return data.pop()

  root = data[0]
  data[0] = data.pop()
  heapify_down(0)
  return root


def heapify_up(i):    
  while i > 0 and data[i] > data[(i - 1) // 2]:
    parent = (i - 1) // 2
    data[i], data[parent] = data[parent], data[i]
    i = parent

def heapify_down(i):
  biggest = i 
  left = (2 * i) + 1
  right = (2 * i) + 2

  if left < len(data) and data[left] > data[biggest]:
    biggest = left
  if right < len(data) and data[right] > data[biggest]:
    biggest = right
  
  if biggest != i:
    data[i], data[biggest] = data[biggest], data[i]
    heapify_down(biggest)

def get_top_k_elements(k):
  data_k_elements = []
  for _ in range(len(data)):
    number = pop()
    if number not in data_k_elements:
        if len(data_k_elements) >= k:
          break
        data_k_elements.append(number)  
  return data_k_elements
          
# =====================
# 🧪 TESTES (asserts)
# =====================

# Test 1 — simple example 
arr = [1,2,3,4,5,6,7,8,9,10,3,1,10,3,10,7,10]
data.clear()
for n in arr:
    insert(n)
assert get_top_k_elements(3) == [10, 9, 8], "Error: expected [10, 9, 8]"

# Test 2 — All values are equal
arr = [5, 5, 5, 5]
data.clear()
for n in arr:
    insert(n)
assert get_top_k_elements(2) == [5], "Error: expected [5]"

# Test 3 — Order decreasing
arr = [9, 8, 7, 6, 5]
data.clear()
for n in arr:
    insert(n)
assert get_top_k_elements(2) == [9, 8], "Error: expected [9, 8]"

# Test 4 — A few elements
arr = [1, 2]
data.clear()
for n in arr:
    insert(n)
assert get_top_k_elements(5) == [2, 1], "Error: expected [2, 1]"

print("✅ All asserts passed successfully!")


