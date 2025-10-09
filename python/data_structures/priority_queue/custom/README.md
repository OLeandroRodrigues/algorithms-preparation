# 🧩 Custom Priority Queue

This folder contains a **manual implementation** of a Priority Queue using a custom-built `MaxHeap`.

- The `MaxHeap` is implemented from scratch (no built-in libraries).
- Each element is stored as a tuple `(priority, -order, value)` to ensure:
  - **Max-priority behavior** (highest priority first)
  - **Stability** (FIFO among equal priorities)

**Complexities:**
- `push`: O(log n)
- `pop`:  O(log n)
- `peek`: O(1)

📘 Reference: *Introduction to Algorithms* (Cormen et al., 4th Edition, Chapter 6)