class Queue:

    def __init__(self) -> None:
        """
        Initializes an empty queue.

        post: creates an instance of Queue with an empty list as data storage.
        """
        self._data = []

    def enqueue(self, item) -> None: 
        """
        Add new element to the back of the queue.

        post: appends the item to the end of the queue.
        """
        self._data.append(item)    

    def dequeue(self):
        """
        Remove and return element from the front of the queue.

        pre: he queue must not be empty.
        post: removes and returns the element at index 0 from the queue.
        """
        assert not self.is_empty(), "Cannot dequeue from an empty queue"
        return self._data.pop(0)

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        post: returns True if the queue is empty, False otherwise.
        """
        return len(self._data) == 0

    def clear(self) -> None:
        """
        Clears the queue, removing all elements.

        post: removes all elements from the queue.
        """
        self._data.clear()
