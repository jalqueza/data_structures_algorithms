def bubble_sort(array):
    # Worse O(nlog(n))
    # Best O(n)
    
    for i in range(len(array)):
        swaps = 0
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j] 
                array[j] = temp
                swaps += 1
        if swaps == 0:
            return array
        
    return array

def selection_sort(array):
    # Worse O(n)
    # Best O(n)
    
    for i in range(len(array)):
        minimum = array[i]
        minimum_index = i
        for j in range(i + 1, len(array)):
            if array[j] > minimum:
                minimum_index = j
        temp = array[i]
        array[i] = minimum
        array[minimum_index] = temp
            
    return array


def insertion_sort(array):
    # Best O(n)
    # Worse O(n^2)
    
    for i in range(len(array)):
        current = array[i]
        
        if current < array[0]:
            # shift all items from index 0 to i to the right one
            swap = array[0]
            for k in range(i):
                temp = array[k+1]
                array[k+1] = swap
                swap = temp
            # insert in correct position
            array[0] = current              
        else:
            # go down previously sorted partial array
            for j in range(i, -1, -1):
                if ((current < array[j] and current > array[j-1]) or
                    (current == array[j-1])):
                        # shift all items from index j to i to the right one
                        swap = array[j]
                        for k in range(j, i):
                            # O(1)
                            temp = array[k+1]
                            array[k+1] = swap
                            swap = temp
                        # insert in correct position
                        array[j] = current                 

    return array
                
    


def main():    
    #basket1 = [2, 65, 34, 2, 1, 7, 8]
    #basket1.sort()
    #print(basket1)
    
    #array_bubble_sort = [2, 65, 34, 2, 1, 7, 8]
    #print(bubble_sort(array_bubble_sort))    
    
    #array_selection_sort = [2, 65, 34, 2, 1, 7, 8]
    #print(bubble_sort(array_selection_sort))    
    
    
    array_insertion_sort = [1, 3, 5, 6, 7, 8, 2, 4]
    print(insertion_sort([2, 65, 34, 2, 1, 7, 8]))        
    
    
    
    
    

    return
    
if __name__ == "__main__":
    main()