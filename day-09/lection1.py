#Dynamic Class and Instance Attributes
# class Car:

class User:
    pass

Martin = User()
Martin.name = 'Martin'
Martin.age = 25
Martin.position = 'Junior Developer'
Martin.department = 'Software Development'

def __init__(self,name,age,position,department):
    self.name = name
    self.age = age
    self.position = position
    self.department = department

User.__init__ = __init__
User.__dir__

print(f'User , {User.__dict__}')
"""
User , {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'User' objects>, '__weakref__': <attribute '__weakref__' of 'User' objects>, '__doc__': None, '__init__': <function __init__ at 0x7f8b1c1b7d30>}
"""

# example 2

Nicloas = User('Nicloas', 25, 'Senior Developer', 'Software Development')

print(f'Nicloas , {Nicloas.__dict__}')
""" 
Nicloas , {'name': 'Nicloas', 'age': 25, 'position': 'Senior Developer', 'department': 'Software Development'}
"""






class Record:
    """
    This class is used to store the record of the student   
    Attributes:
    name: str: the name of the student
    age: int: the age of the student
    """
bob ={
    'name':'Bob Uncle',
    'age':25,
    "position":'Software Developer',
    "department":'Software Development',
    "salary": 50000,
    "is_manager": False

}

fielx_record = Record()

for field ,value in bob.items():
    setattr(fielx_record,field,value)
##const student = Record('John', 25)


print(f'fielx_record.name, {fielx_record.name}')
print(f'fielx_record __dic___, {fielx_record.__dict__}')
