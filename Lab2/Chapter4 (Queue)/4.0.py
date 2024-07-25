# First In First Out (FIFO)
# <-- [] <--

class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enQueue(self, data):
        self.queue.append(data)

    def deQueue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return None
        
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return str(self.queue)