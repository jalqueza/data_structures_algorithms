class Array:
    
    def __init__(self, data):
        self.data = data
    
    def index(self, item): 
        # O(n)
        for i in range(len(self.data)):
            if self.data[i] == item:
                return i
        return None

    def append(self, item): 
        # O(1)
        self.data += [item]
    
    def insert(self, index, item): 
        # O(n)
        self.data = self.data[:index] + [item] + self.data[index:] #slicing is O(n)
            
    def remove(self, item): 
        # O(n)
        for i in range(len(self.data)):
            if self.data[i] == item:
                del self.data[i]
                break

def reverse(string):
    # O(n)
    reversed_string = ""        
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string

def merge_sorted_arrays(array1, array2):
    #O(len(array1) + len(array2))
    merged_array = []
    i, j = 0, 0 # two indices
    while i < len(array1) and j < len(array2):        
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i+=1
        else:
            merged_array.append(array2[j])
            j+=1
    return merged_array + array1[i:] + array2[j:]
    
                
def main():
    
    # 62
    array1 = ["a", "n", "c", "z"]
    
    ''' 
    array1 is has 4 items, so in a 32 bit system
    this would take 4*4 bytes = 16 bytes of storage
    '''
    array1.append("a")     # O(1)
    array1.index("a")      # O(n)
    array1.insert(2, "2")  # O(n)
    array1.remove("a")     # O(n)
    print(array1)
    
    array2 = Array(["a", "n", "c", "z"])
    array2.append("a")     # O(1)
    array2.index("a")      # O(n)
    array2.insert(2, "2")  # O(n)
    array2.remove("a")     # O(n)    
    print(array2.data)
    
    print(reverse("abc"))
    print(merge_sorted_arrays([], [4,6,30]))

    
if __name__ == "__main__":
    main()