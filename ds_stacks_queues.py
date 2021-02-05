class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    def peek(self):    
        # O(1)
        return None if self.last == None else self.last.value
    
    def enqueue(self, value):
        # O(1)
        node = Node(value)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1    
        return self
    
    def dequeue(self):
        # O(1)
        if self.length == 0:
            return None
        else:
            dequeued = self.first.value
            self.first = self.first.next
            if self.first == self.last:
                self.last = None            
            self.length -= 1
            return dequeued

class StackLL:
    # stack implemented using linked list
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
        
    def peek(self):    
        # O(1)
        return None if self.top == None else self.top.value
    
    def push(self, value):
        # O(1)
        node = Node(value)
        node.next = self.top
        self.top = node
        return self.top
    
    def pop(self):
        # O(1)
        if self.top == None:
            return None
        else:
            self.top = self.top.next
            self.length -= 1
        return

class StackArray:
    def __init__(self):
        self.array = []
        
    def peek(self):    
        # O(1)
        return None if len(self.array) == 0 else self.array[len(self.array)-1]
    
    def push(self, value):
        # O(1)
        self.array.append(value)
        return self.array
    
    def pop(self):
        # O(1)
        self.array.pop()
        return self.array
    
def main():
    
    letters = []
    letters.append('c')
    letters.append('a')
    letters.append('t')
    letters.append('g')
    last_item = letters.pop()
    print(last_item)    
    
    # QUEUE
    fruits = []
    fruits.append('banana')
    fruits.append('grapes')
    fruits.append('mango')
    fruits.append('orange')
    fruits.
    first_item = fruits.pop(0)
    print(first_item)
    
if __name__ == "__main__":
    main()