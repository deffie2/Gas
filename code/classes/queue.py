class Queue:

    def __init__(self):
        self._data = []

    def enqueue(self, element):
        """Add new element to back of queue"""
        self._data.append(element) 

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
