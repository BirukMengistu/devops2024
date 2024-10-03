
uservalue= input(f'hey user , enter value ')
#gloabal variable
units =['cm','inch' ,'meter']

def converter(value, unit):
    if unit=='cm':
     return f'converting value {value*0.1} {unit}'
    elif unit=='inch':
     return f'converting value {value}  {value*0.1} {unit}'
    else:
     return (f'check input value')


result = converter(100, units[1])
print(f'result ->' , result)
converter(100, units[0])
