#name conventions
first_name='boo'
lastName='tech'
firstName='dev'
lastdigt2=''
#1 onfirst digit not acceptable
# 2nameofvarabel
firstdigit=''
#concate name

print(first_name + firstName)

#string bulitin function

sizeofName = firstName.__sizeof__()
countChar= firstName.count('v')
upperCase=firstName.upper()
concatName= first_name + lastName
#captalize the first char
captalize=firstName.capitalize()
print(sizeofName ,countChar , captalize ,upperCase)
# concat string
print(concatName)
#format for string
print('Hello my full name','->' + firstName.capitalize() + ' ' + lastName.capitalize() )