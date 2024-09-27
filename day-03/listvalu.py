
name_of_unit = ['mint','second', 'inch']
hour=24
Miuntes=60
second=60
def display_no_min_day(value, unit):
   print(f'20 day are {value * hour *Miuntes} {unit}')

def displayNumberSecondOfdays(value, unit):
   print(f'20 day are {value * hour *Miuntes} {unit}')


def validate_and_ect (user_input):
    
    if int(user_input) >0:
      return display_no_min_day(user_input,name_of_unit[1])
    elif int(user_input) == 0:
      return display_no_min_day(user_input,name_of_unit[2])
    else:
       return f'user input not valid'
    

input_value=''
while input_value != 'exist':
   user_input = input('inter value \n')
   for x in user_input.split():
     validate_and_ect(x)