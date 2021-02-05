# use closure to keep the cache inside the function
def memoize():
    cache = {}
    
    def add_80(n):
        if n in cache:
            print("using cache")
            return cache[n]
        cache[n] = n + 80
        return cache[n]
    
    return add_80

#memoized_function = memoize()
#print(memoized_function(5))
#print(memoized_function(5))
#print(memoized_function(5))


# 0 1 2 3 5 8 13 21 34 fibonnaci


def memoize_fib():
    cache = {}
    
    def fibonacci(n):
        if n-2 in cache and n-1 in cache:
            print("using cache")
            cache[n] = cache[n-2] + cache[n-1]
            return cache[n]
        elif n < 2:
            cache[n] = n
            return cache[n]
        else:
            for i in range(2, n+1):
                # O(n)
                if i not in cache:
                    cache[i] = cache[i-2] + cache[i-1]
        return cache[n]
    
    return fibonacci
    
memoized_fib = memoize_fib()
print(memoized_fib(0))
print(memoized_fib(1))
print(memoized_fib(2))
print(memoized_fib(3))
print(memoized_fib(4))
print(memoized_fib(5))
print(memoized_fib(6))


def fibonnaci_master(n):
    # top down technique
    
    answer = [0, 1]
    for i in range(2, n+1):
        answer.append(answer[i-2] + answer[i-1])
    return answer.pop()

print(fibonnaci_master(6))