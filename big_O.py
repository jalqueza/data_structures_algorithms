def contains_common_item(array1, array2):
    if len(array1) < 1 and len(array2) < 1:
        return False
    for item in array1:
        if item in array2:
            return True
    return False

def print_all_numbers_then_pair_sums(numbers):
    
    for number in numbers:
        print(number)
        
    for number1 in numbers:
        for number2 in numbers:
            print(number1 * numbers2)
    
    # O(n^2) = ~O(n + n *n)
    

def findNemo(input):
    nemo = ["not_nemo" * 7] + ["nemo"]
    for i in range(len(nemo)):
        if nemo[i] == "nemo":
            return nemo[i]
        
    return None

def fun_challenge(input):
    a = 10 # O(1)
    a = 50 + 3 # O(1)
    
    for i in range(len(input)): # O(n)
        another_function(); # O(n)
        stranger = True  # O(n)
        a += 1 # O(n)
        
    for i in range(len(input)): # O(n)
        another_function(); # O(n)
        stranger = True  # O(n)
        a += 1 # O(n)    
    
    return a # O(1)
    
    # overall: O(n) = ~O*(3 + 8n)
    
    
# Find 1st, Find Nth...
tweets = ["hi", "my", "teddy"]
first = tweets[0] # O(1)
nth = tweets[len(tweets) - 1]
    
if __name__ == "__main__":
    main()