import heapq


class PriorityQueue:
	def __init__(self):
		self._queue = []

	def is_empty(self):
		return len(self._queue) == 0

	def size(self):
		return len(self._queue)

	def push(self, item, priority):
		heapq.heappush(self._queue, (-priority, item))

	def pop(self):
		if self.is_empty():
			raise IndexError("The priority queue is empty.")
		return heapq.heappop(self._queue)[-1]

	def clear(self):
		self._queue.clear()


if __name__ == "__main__":
	
	pq = PriorityQueue()
	pq.push("Task 1", 1)
	pq.push("Taks2", 4)
	pq.push("Task 3", 2)

	print(pq.pop())
	print(pq.pop())
	print(pq.pop())