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
        # O(log(n))
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
        # O(log(n))
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
    
    def breadth_first_search(self):
        # O(n)
        current_node = self.root
        traversal_list = []
        queue = []
        queue.append(current_node)
        
        while len(queue) != 0:
            current_node = queue.pop(0)            
            traversal_list.append(current_node.value)
            if current_node.left != None:
                queue.append(current_node.left)
            if current_node.right != None:
                queue.append(current_node.right)            
            
        return traversal_list
    
    def recursive_breadth_first_search(self, queue, traversal_list):
        # O(n)
        if len(queue) == 0:
            return traversal_list
        
        # add children to queue
        current_node = queue.pop(0)
        traversal_list.append(current_node.value)
        if current_node.left != None:
            queue.append(current_node.left)
        if current_node.right != None:
            queue.append(current_node.right)
        
        return self.recursive_breadth_first_search(queue, traversal_list)

    def depth_first_search_in_order(self):
        return traverse_in_order(self.root, [])
    
    def depth_first_search_pre_order(self):
        return traverse_pre_order(self.root, [])
    
    def depth_first_search_post_order(self):
        return traverse_post_order(self.root, [])
        

def traverse_in_order(node, array):
    # O(n)
    if node.left != None:
        traverse_in_order(node.left, array)
    array.append(node.value)
    if node.right != None:
        traverse_in_order(node.right, array)    
    return array

def traverse_pre_order(node, array):
    # O(n)
    array.append(node.value)
    if node.left != None:
        traverse_pre_order(node.left, array)
    if node.right != None:
        traverse_pre_order(node.right, array)    
    return array

def traverse_post_order(node, array):
    # O(n)
    if node.left != None:
        traverse_post_order(node.left, array)
    if node.right != None:
        traverse_post_order(node.right, array)
    array.append(node.value)
    return array
        
def main():
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(20)
    tree.insert(1)
    tree.insert(6)
    tree.insert(15)
    tree.insert(170)
    
    print(tree.breadth_first_search())
    print(tree.recursive_breadth_first_search([tree.root], []))
    
    print(tree.depth_first_search_in_order())
    print(tree.depth_first_search_pre_order())
    print(tree.depth_first_search_post_order())
    
    return
    
if __name__ == "__main__":
    main()