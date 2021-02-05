def find_factorial_recursive(number):
    # O(2^n)
    
    if number == 1:
        return number
    else:
        return number * find_factorial_recursive(number - 1) 
        

def find_factorial_iterative(number):
    # O(n)
    
    answer = 1
    for i in range(number, 1, -1):
        answer = answer * i
        
    return answer

def fibonacci_recursive(n):
    # O(2^n)
    
    if n < 2:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    # O(n)
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-2] + sequence[i-1])
    
    return sequence[n-1]

def reverse_string_recursive(string):
    
    if len(string) == 1:
        return string
    return string[len(string) - 1] + reverse_string_recursive(string[:len(string)-1]) 
    


def main():    
    print(reverse_string_recursive("string"))    
    return
    
if __name__ == "__main__":
    main()