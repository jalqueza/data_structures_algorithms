class Hash:
    
    def __init__(self, data):
        self.data = data
        
    def hash_key():
        return random.randint(len(self.data)) # should be same output
    
    def set(self, key, value): 
        # O(1)
        this.data[hash_key()] = [key, value]

    def get(self, key): 
        # O(1)
        return self.data[key]

    def keys():
        keys = []
        for item in self.data:
            keys.append(item[0])
        return keys

def first_recurring_character(array):
    # O(n)
    integer_instances = {}
    for item in array:
        if item in integer_instances:
            return item
        else:
            integer_instances[item] = True
    return None
                
def main():
    
    dictionary = {
        "age": 54,
        "name": "Lebron",
        "magic": True,
    }
    
    print("age" in dictionary)         # search O(1)
    print(dictionary["age"])           # lookup O(1)
    dictionary["last_name"] = "James"  # insert O(1)
    del dictionary["magic"]            # delete O(1)
    print(dictionary)
    print(dictionary.values())
    
    print(first_recurring_character([2,5,1,2,3,5,1,2,4]))
    print(first_recurring_character([2,1,1,2,3,5,1,2,4]))
    print(first_recurring_character([2,3,4,5]))
    
if __name__ == "__main__":
    main()