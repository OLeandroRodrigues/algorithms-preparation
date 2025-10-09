# ⚙️ Built-in Priority Queue

This folder contains a Priority Queue implementation using **Python’s standard library** (`heapq`).

- Uses `heapq` (binary min-heap) for efficient O(log n) operations.
- Stability guaranteed via `itertools.count()` as a tiebreaker.
- Can operate as a **min-priority** or **max-priority** queue (`is_min` flag).

**Complexities:**
- `push`: O(log n)
- `pop`:  O(log n)
- `peek`: O(1)

**Why this version?**
To compare performance and readability against the custom MaxHeap-based implementation.