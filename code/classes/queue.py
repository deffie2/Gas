class Queue:

    def __init__(self):
        self._data = []
        self.visited_state = set()

    def enqueue(self, item):
        """Add new element to back of queue if not visited"""
        item_hash = hash(item)
        if item_hash not in self.visited_state:
            self._data.append(item)
            self.visited_state.add(item_hash)

    def dequeue(self):
        """Remove and return element from front of queue"""
        assert not self.is_empty(), "Cannot dequeue from an empty queue"
        return self._data.pop(0)

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self._data) == 0

    def clear(self) -> None:
        """Clears the queue, removing all elements"""
        self._data.clear()
        self.visited_state.clear()
