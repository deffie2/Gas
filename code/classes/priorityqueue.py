import heapq
from typing import Any, List, Tuple
from code.classes.board import Board


class PriorityQueue:

    def __init__(self) -> None:
        """
        Initializes the priority queue.

        Post: a new empty priority queue is created.
        """
        self._queue: List[Board] = []

    def is_empty(self) -> bool:
        """
        Checks if the priority queue is empty.

        post: returns True if the priority queue contains no elements,
        otherwise False.
        """
        return len(self._queue) == 0

    def size(self) -> int:
        """
        Returns the size of the priority queue.

        Post: Returns the number of elements currently in the priority queue.
        """
        return len(self._queue)

    def push(self, item: Board, priority: int) -> None:
        """
        Adds an item to the priority queue with a specified priority.

        Pre: priority must be an integer.

        Post: the item is added to the priority queue with the specified
        priority.
        """
        assert isinstance(priority, int), "Priority must be an integer."
        heapq.heappush(self._queue, (-priority, item))

    def pop(self) -> Board:
        """
        Removes and returns the item with the highest priority.

        Pre: the priority queue must not be empty.

        Post: the board state with the highest priority is removed from the
        priority queue and returned.
        Post: Raises an IndexError if the priority queue is empty.
        """
        assert not self.is_empty(), "The priority queue must not be empty."
        return heapq.heappop(self._queue)[-1]

    def clear(self) -> None:
        """
        Clears all items from the priority queue.

        Post: all items are removed from the priority queue.
        """
        self._queue.clear()
