let =('boo', 'd',4 , 56)
listBox=['boo', 'd',4 , 56]
print(f'let {let}')
print(f'length let tuple -> {len(let)}')
print(f'length let list -> {len(listBox)}')
print(f'typeof {type(let)}')
print(f'typeof {type(listBox)}')



def check_type(props):
    if(isinstance(props ,tuple)):
        return f'input props - {props}  , tuple'
    elif(isinstance(props, list)):
        return f'input props - {props}  , list'
    else:
        return f'input props - {props}  , unknow'
    

print(check_type(let))
print(check_type(listBox))
print(check_type(True))