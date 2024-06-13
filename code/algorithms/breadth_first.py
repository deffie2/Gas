from code.classes.board import Board
from code.classes.vehicle import Vehicle
from code.classes.queue import Queue


def breadth_first_search_without_heur(initial_bord):
	# Create een queue om toestanden van het bord en bijbehorende moves te beheren
	queue = Queue
	# Bijhouden van welke bordtoestanden zijn al geweest, dit voorkont herhaling
	visited_state = set()

	# Iets in de queue zetten
	queue.enqueue(initial_bord, [])

	



	visited_state.add(initial_bord)


def breadth_first_search_with_heur():
	pass

