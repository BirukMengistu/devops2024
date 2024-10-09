#map() with Lambda Expressions

# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# Add two lists using map and lambda

numbers1 = [1, 2, 3]        
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)    
print(list(result))
