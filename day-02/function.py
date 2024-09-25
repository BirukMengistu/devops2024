def my_function():
    print('hello from a function')

my_function()

#function argument

def my_functionarg(name):
    print('name',name)
#function parameter
my_functionarg('boo')

#Arbitrary Arguments, *args

def my_functionArg(*props):
    print('the youngest child',props[2])

my_functionArg('boo','tome', 'melo')

#You can also send arguments with the key = value syntax.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 

#If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes") 

#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 
