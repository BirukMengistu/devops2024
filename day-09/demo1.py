#map Function
# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)

"""
map(func, *iterables) --> map object

Make an iterator that computes the function using arguments from
each of the iterables. Stops when the shortest iterable is exhausted.
"""
result = map(addition, numbers)
print(list(result))


# recursive function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(f'factorial(5)',factorial(5))
print(f'factorial(4)',factorial(4))

