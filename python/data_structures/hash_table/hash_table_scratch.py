class HashTable:
    class Node:
        def __init__(self, key, value, next=None):
            self.key = key
            self.value = value
            self.next = next

    def __init__(self, capacity=8, load_factor=0.75):
        self.capacity = capacity
        self.size = 0
        self.load_factor = load_factor
        self.buckets = [None] * capacity

    # -----------------------------
    #      Internal helpers
    # -----------------------------
    def _hash(self, key):
        """Raw Python hash converted to non-negative."""
        return hash(key) & 0x7FFFFFFF

    def _index(self, key):
        return self._hash(key) % self.capacity

    def _needs_rehash(self):
        return self.size / self.capacity >= self.load_factor

    def _rehash(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self.size = 0

        for node in old_buckets:
            current = node
            while current:
                self.put(current.key, current.value)
                current = current.next

    # -----------------------------
    #       Public operations
    # -----------------------------
    def put(self, key, value):
        """Insert or update a key-value pair."""
        if self._needs_rehash():
            self._rehash()

        index = self._index(key)
        head = self.buckets[index]

        current = head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = HashTable.Node(key, value, head)
        self.buckets[index] = new_node
        self.size += 1

    def get(self, key):
        """Return value for key. Raises KeyError if not found."""
        index = self._index(key)
        current = self.buckets[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(f"Key not found: {key!r}")

    def remove(self, key):
        """Remove key. Returns True if removed, False otherwise."""
        index = self._index(key)
        current = self.buckets[index]
        prev = None

        while current:
            if current.key == key:
                if prev is None:
                    self.buckets[index] = current.next
                else:
                    prev.next = current.next

                self.size -= 1
                return True

            prev = current
            current = current.next

        return False

    def contains(self, key):
        """Check if key exists."""
        index = self._index(key)
        current = self.buckets[index]

        while current:
            if current.key == key:
                return True
            current = current.next

        return False

    def __len__(self):
        return self.size

    def __repr__(self):
        pairs = []
        for bucket in self.buckets:
            current = bucket
            while current:
                pairs.append(f"{current.key}: {current.value}")
                current = current.next
        return "{ " + ", ".join(pairs) + " }"

