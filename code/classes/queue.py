class Queue:

    def __init__(self):
        self.items = []  # Initialiseert een lege lijst voor de queue.

    def isEmpty(self):
        return len(self.items) == 0  # Controleert of de queue leeg is. Geeft True terug als leeg, anders False.

    def enqueue(self, item):
        self.items.insert(0, item)  # Voegt een nieuw item toe aan het begin van de queue.

    def dequeue(self):
        return self.items.pop()  # Verwijdert en retourneert het laatste item (het oudste item) uit de queue.

    def size(self):
        return len(self.items)  # Geeft het aantal items in de queue terug.

    def clear(self) -> None:
        self.items.clear()  # Leegt de queue door alle items te verwijderen.