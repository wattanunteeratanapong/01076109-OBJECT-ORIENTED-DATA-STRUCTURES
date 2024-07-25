# Last In First Out (LIFO)
# [] <--
# [] -->

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0
        
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None
    
    def size(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)