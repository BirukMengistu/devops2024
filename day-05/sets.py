set_value={ 1,2,3,4,5,6,7,8,9,10}
set_value1 = {11,12,13,14,1,5,3,4}
#x = set_value[1] # error
set_value.add(11)
set_value.remove(1)

print(f'set_value: {set_value}')
#set functions
union = set_value.union(set_value1)
print(f'union: {union}')
#difference = set_value.difference(set_value1)
intersection = set_value.intersection(set_value1)
print(f'intersection: {intersection}')
print(f'set_value: {set_value}')

