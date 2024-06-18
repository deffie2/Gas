import heapq


class PriorityQueue:
	def __init__(self):
		self._queue = []

	def is_empty(self):
		return len(self._queue) == 0

	def size(self):
		return len(self._queue)

	def push(self, item, priority):
		heapq.heapqpush(self._queue, (-priority, item))

	def pop(self):
		if self.is_empty():
			raise IndexError("The priority queue is empty.")
		return heapq.heappop(self._queue)[-1]

	def peek(self):
		f self.is_empty():
			raise IndexError("The priority queue is empty.")
		return self._queue[0][-1]


if __name__ == "__main__":
	
	pq = PriorityQueue()
	pq.push("Task 1", 1)
	pq.push("Taks2", 3)
	pq.push("Task 3", 2)

	print(pq.pop())
	print(pq.pop())
	print(pq.pop())