

#gloabal variable
units =['cm','inch' ,'meter']

def converter(value, unit):
    try:
        uservalue= int(input(f'hey user , enter value '))
        if(type(uservalue)!=str and int(uservalue) > 0):
            if unit=='cm':
             return f'converting value {value*0.1} {unit}'
            elif unit=='inch':
             return f'converting value {value}  {value*0.1} {unit}'
            else:
             return (f'check input value')
        else:
            return f'input needs to string'   

    except ValueError:
      return (f'instant of value error')

    

      
result = converter(100, units[1])
print(f'result ->' , result)
while True:
 result = converter(100, units[0])
 print(f'result ->' , result)