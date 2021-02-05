class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DLinkedList:
    # Doubly Linked List
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = 0

        if value != None:
            node = Node(value)
            node.next = self.head
            self.head = node
            self.tail = node
            self.length += 1
            
    def prepend(self, value):
        # O(1)
        node = Node(value)
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node
        if self.tail == None:
            self.tail = self.head
        self.length += 1

    def append(self, value):
        # O(1)
        node = Node(value)
        node.prev = self.tail # doubly
        
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            
        self.length += 1
        
        return self

    def insert(self, index, value):
        # O(n)
        if index > self.length:
            raise RangeError('index out of bounds')
        
        if index == 0:
            self.prepend(value)
            return self
        
        current_node = self.head
        for i in range(index - 1):
            current_node = current_node.next
        
        node = Node(value)
        node.prev = current_node
        node.next = current_node.next
        current_node.next = node
        
        if node.next != None:
            node.next.prev = node
        
        self.tail = node
        
        self.length += 1
        
        return self

    def delete(self, index):
        # O(n)
        if index > self.length:
            raise RangeError('index out of bounds')
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return self
        
        delete_node = self.head
        prev = None
        for i in range(index):
            prev = delete_node
            delete_node = delete_node.next
        
        if index == self.length - 1:
            self.tail = prev
            self.tail.next = None
        else:
            prev.next = delete_node.next
            if delete_node.next != None:
                delete_node.next.prev = prev
            
        self.length -= 1

        return self

    def print_list(self):
        # O(n)
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
    
    def print_list_reverse(self):
        # O(n)
        current = self.tail
        while current != None:
            print(current.value)
            current = current.prev    
            
    def search(self, value):
        # O(n)
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next 
        
        return False

class SLinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = 0

        if value != None:
            node = Node(value)
            node.next = self.head
            self.head = node
            self.tail = node
            self.length += 1
            
    def prepend(self, value):
        # O(1)
        node = Node(value)
        node.next = self.head
        
        self.head = node
        if self.tail == None:
            self.tail = self.head
        self.length += 1

    def append(self, value):
        # O(1)
        node = Node(value)
        
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            
        self.length += 1
        
        return self

    def insert(self, index, value):
        # O(n)
        if index > self.length:
            raise RangeError('index out of bounds')
        
        if index == 0:
            self.prepend(value)
            return self
        
        current_node = self.head
        for i in range(index - 1):
            current_node = current_node.next
        
        node = Node(value)
        node.next = current_node.next
        current_node.next = node
        
        self.tail = node
        
        self.length += 1
        
        return self

    def delete(self, index):
        # O(n)
        if index > self.length:
            raise RangeError('index out of bounds')
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return self
        
        delete_node = self.head
        prev = None
        for i in range(index):
            prev = delete_node
            delete_node = delete_node.next
        
        if index == self.length - 1:
            self.tail = prev
            self.tail.next = None
        else:
            prev.next = delete_node.next
            
        self.length -= 1

        return self

    def print_list(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
    
    def reverse(self):
        # O(n)
        prev = None
        current = self.head
        for i in range(self.length):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        self.head = prev
            
        return self
            
    def search(self, value):
        # O(n)
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next 
        
        return False
    
def main():
    
    '''
    apples 
    8293 ---> grapes
              3232 --> pears
                       372 --> null
    '''
    
    obj1 = {"a" : True}
    obj2 = obj1
    #print(obj1, obj2)
    #print(obj1 is obj2)
    #print(obj1 == obj2)
    #print(id(obj1), id(obj2))
    obj2 = None # new memory location
    
    a = 2
    b = 2
    # a and b point to the same object of 2 from different variable memory locations
    b = 3
    b = a # b now has the same variable memory location as a
    a = 2 # b is 2
    b = 3 # b is 3, a is 2
    #print(a,b)
    
    linked_list = SLinkedList(3)
    linked_list.prepend(2)
    linked_list.prepend(1)
    #linked_list.insert(0,0)
    #linked_list.append(6)
    #linked_list.insert(4,4)
    #linked_list.insert(5,5)
    #linked_list.insert(7,7)
    #linked_list.delete(0)
    #linked_list.delete(6)
    #linked_list.delete(4)
    #print(linked_list.search(4))
    #print(linked_list.search(0))
    linked_list.print_list()
    linked_list.reverse()
    print("--")
    linked_list.print_list()
    
    
if __name__ == "__main__":
    main()