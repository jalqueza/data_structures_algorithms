class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        # O(log(n))
        node = BSTNode(value)
        
        if self.root == None:
            self.root = node
            return
        
        current_node = self.root
        while True:
            
            # add to the left
            if value < current_node.value:
                if current_node.left == None:
                    current_node.left = node
                    break
                current_node = current_node.left
                
            # add to the right
            elif value > current_node.value:
                if current_node.right == None:
                    current_node.right = node
                    break
                current_node = current_node.right
                
        return
    
    def lookup(self, value):
        # O(log(N))
        if self.root == None:
            return
        
        current_node = self.root
        while True:
            if value == current_node.value:
                return True
            
            # search left
            if value < current_node.value:
                if current_node.left == None:
                    break
                current_node = current_node.left
                
            # search right
            elif value > current_node.value:
                if current_node.right == None:
                    break
                current_node = current_node.right            
        
        return False
    
    def remove(self, value):
        # O(log(N))
        if self.root == None:
            return
    
        parent_node = None 
        current_node = self.root
        while True:
            
            if value == current_node.value:
                
                # deleted node has no left and right child
                if current_node.left == None and current_node.right == None:
                    if parent_node.left.value == value:
                        parent_node.left = None
                    elif parent_node.right.value == value:
                        parent_node.right = None
                    return
                
                # deleted node has both children https://www.youtube.com/watch?v=wcIRPqTR3Kc
                elif current_node.left != None and current_node.right != None:
                    previous_node = None
                    left_node = current_node.right
                    while True:
                        if left_node.left == None:
                            break
                        previous_node = left_node
                        left_node = left_node.left
                        
                    previous_node.left = None if left_node.right == None else left_node.right
                    current_node.value = left_node.value
                    
                # deleted node has left child
                elif current_node.left != None:
                    if parent_node.right and parent_node.right.value == value:
                        parent_node.left = current_node.left
                    elif parent_node.left and parent_node.left.value == value:                  
                        parent_node.right = current_node.left
                    return            
                
                # deleted node has right child
                elif current_node.right != None:
                    if parent_node.right and parent_node.right.value == value:
                        parent_node.right = current_node.right
                    elif parent_node.left and parent_node.left.value == value:                
                        parent_node.left = current_node.right
                    return  
                    
                
            # search left
            if value < current_node.value:
                if current_node.left == None:
                    break
                parent_node = current_node
                current_node = current_node.left
            
            # search right
            elif value > current_node.value:
                if current_node.right == None:
                    break
                parent_node = current_node
                current_node = current_node.right
                
        return         
        
    
def level_order_traverse(rootnode):
    thislevel = [rootnode]
    while thislevel:
        nextlevel = list()
        for n in thislevel:
            print(n.value)
            if n.left: nextlevel.append(n.left)
            if n.right: nextlevel.append(n.right)
        print
        thislevel = nextlevel
        
def main():
    tree = BinarySearchTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(40)
    tree.insert(20)
    tree.insert(60)
    tree.insert(80)
    tree.insert(32)
    tree.insert(34)
    tree.insert(65)
    tree.insert(36)
    tree.insert(85)
    tree.insert(75)
    
    tree.remove(30)
    level_order_traverse(tree.root)
    
    return
    
if __name__ == "__main__":
    main()