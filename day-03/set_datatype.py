#set data type
""" Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed. """
import json
store = ['a', 'b' ,1, 4]
biblotake =[{
    'name':'book',
     'age':34,
     'sex':'male'
},{
    'name':'cat',
     'age':24,
     'sex':'male'
}]
#dic_bibilotake = json.loads(biblotake)

print(f'{biblotake}')
for x in store:
    print(f'value : {x}')

for x in biblotake:
    print (f'bibilotak -name {x}')