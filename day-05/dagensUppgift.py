
#list name

list_name={'dog':'Max','cat':'Tom','bird':'Tweety','fish':'Goldie'}
size=0
#display the list of animals

def display_animal():
    print('List of animals:')
    index=1
    for key in list_name:
        print(f'{index} key {key} value {list_name[key]}')
        index+=1

def add_animal():
    animal_name = input('Enter animal name: ')
    list_name[animal_name] = animal_name
    print('Animal added successfully')
def remove_animal():
    animal_name = input('Enter animal name: ')
    if animal_name in list_name:
        del list_name[animal_name]
        print('Animal removed successfully')
    else:
        print('Animal not found')
def set_of_size():
     global size 
     size = int(input('Enter the size of set: '))

def create_group(): 
    group = set()
    if size==0:
        print('Enter the size of set first')
        return  set_of_size()
    else:
        for key in range(size):
            name = input('input name')
            type = input('input type of animal as unmber  range[1-5]')
            group[name]=name
            group[type]=type
        print(f'group: {group}')
    

print('Welcome to animal management system')
def display_menu():
    print('1. Add animal')
    print('2. Remove animal')
    print('3. Display animal')
    print('4.  set of size of animals')
    print('5. create group of animals')
    print('6. Exit')
    print(f'size: {size}')
    choice = input('Enter your choice: ')
    if choice=='1':
       return add_animal()
    elif(choice=='2'):   
        return remove_animal()
    elif(choice=='3'):
        return display_animal()
    elif(choice=='4'):
         return  set_of_size()
    elif(choice=='5'):
        return create_group()
    elif(choice=='6'):
        return exit()

#display the menu
while True:
 display_menu()

