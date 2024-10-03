
complexbety='The complex data type in python consists of two values, the first one is the real part of the complex number, and the second one is the imaginary part of the complex number.'

#function string datatype
def StringDef():
  print(f'Python, strings are used for representing textual data. A string is a sequence of characters enclosed in either single quotes ('') or double quotes (“”).')
#function number datatype
def Numberdef():
  print(f'Python numbers are a fundamental data type for representing and manipulating numerical values. The three main forms of numbers in Python are integers, floating-point numbers, and complex numbers.')
  
#function Boolean datatype
def Booleandef():
  print(f'Boolean variable can have only two values - True or False. Or in other words, if a variable can have only these two values, we say that it s a Boolean variable.')
  
#function complex datatype
def Booleandef():
  print(f'Boolean variable can have only two values - True or False. Or in other words, if a variable can have only these two values, we say that it s a Boolean variable.')

#function complex datatype
def Complexdef():
  print(f'The complex data type in python consists of two values, the first one is the real part of the complex number, and the second one is the imaginary part of the complex number.') 
def mainMenu():
   print(f'\n')
   print(f'option 1: defin for sting')
   print(f'option 2: defin for number')
   print(f'option 3: defin for boolean')
   print(f'option 4: defin for boolean')
   print(f'option 5: defin for boolean')
while True:
   mainMenu()
   val = int(input('Menu list \n'))
   if val == 1:
     print('string defintion \n')
     StringDef()
   elif val == 2:
      print('number defintion \n')
      Numberdef()
   elif val == 3:
     Booleandef()
   elif val == 4:
     Booleandef()
   elif val == 5:
     Complexdef()
   else:
     print('not option')
     
