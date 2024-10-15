# advance concept

# iterating through an itertor
# Python | Difference between iterable and iterator


""" Iterable is an object, that one can iterate over. It generates an Iterator when passed to iter() method. An iterator is an object, which is used to iterate 
over an iterable object using the __next__() method. """
my_list =[1, 2,3,5]
# code
# next("GFG")  
# # next("GFG") TypeError: 'str' object is not an iterator

test_iter = iter(my_list)
test_iter
print(test_iter) # <list_itertor object at 0x--->

# code 
s="GFG"
s=iter(s)
print(s)
print(next(s))
print(next(s))
print(next(s))


#example list
# list of cities
cities = ["Berlin", "Vienna", "Zurich"]

# initialize the object
iterator_obj = iter(cities)

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))

# example 3
# Function to check object
# is iterable or not
def it(ob):
    try:
        iter(ob)
        return True
    except TypeError:
        return False

# Driver Code
for i in [34, [4, 5], (4, 5),{"a":4}, "dfsdf", 4.5]:
	print(i,"is iterable :",it(i))





#Module 