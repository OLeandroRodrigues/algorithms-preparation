"""
Problem: Find the k largest elements in an array.

Approach:
  - From Scratch: implement a max-heap of size k.
  - Repo-based: reuse your MaxHeap (max depending on design).

Complexity:
  - Time: O(n log k)
  - Space: O(k)
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from python.data_structures.heap.max_heap import MaxHeap

hp = MaxHeap()

def get_top_k_elements(k):
  data_k_elements = []
  for _ in range(len(hp._data)):
    number = hp.pop()
    if number not in data_k_elements:
        if len(data_k_elements) >= k:
          break
        data_k_elements.append(number)  
  return data_k_elements

arr = [1,2,3,4,5,6,7,8,9,10,3,1,10,3,10,7,10]
for n in arr:
    hp.insert(n)

# =====================
# 🧪 TESTES (asserts)
# =====================

# Test 1 — simple example 
arr = [1,2,3,4,5,6,7,8,9,10,3,1,10,3,10,7,10]
hp._data.clear()
for n in arr:
    hp.insert(n)
assert get_top_k_elements(3) == [10, 9, 8], "Error: expected [10, 9, 8]"

# Test 2 — All values are equal
arr = [5, 5, 5, 5]
hp._data.clear()
for n in arr:
    hp.insert(n)
assert get_top_k_elements(2) == [5], "Error: expected [5]"

# Test 3 — Order decreasing
arr = [9, 8, 7, 6, 5]
hp._data.clear()
for n in arr:
    hp.insert(n)
assert get_top_k_elements(2) == [9, 8], "Error: expected [9, 8]"

# Test 4 — A few elements
arr = [1, 2]
hp._data.clear()
for n in arr:
    hp.insert(n)
assert get_top_k_elements(5) == [2, 1], "Error: expected [2, 1]"

print("✅ All asserts passed successfully!")





