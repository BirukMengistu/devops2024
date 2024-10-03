
uservalue= int(input(f'hey user , enter value '))
#gloabal variable
units =['cm','inch' ,'meter']
print(f'input', type(uservalue)==str)
def converter(value, unit):
    if(type(uservalue)!=str and int(uservalue) > 0):
        if unit=='cm':
         return f'converting value {value*0.1} {unit}'
        elif unit=='inch':
         return f'converting value {value}  {value*0.1} {unit}'
        else:
         return (f'check input value')
    else:
      return f'input needs to string'


result = converter(100, units[1])
print(f'result ->' , result)
converter(100, units[0])
