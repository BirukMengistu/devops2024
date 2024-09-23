lastName='tech'
firstName='dev'

# string format

fullName = 'name ->' + firstName +'' + lastName
# complex format

outputTest1 = 'hello , {} {}'.format(firstName ,lastName)
outputTest2 = 'hello , {0} {1}'.format(firstName ,lastName)
print('complex string format -1' ,outputTest1 )
print('complex string format -2',outputTest2)

# complex format payton 3 version

outputTest3 = f'hello, {firstName} {lastName}'

print(outputTest3)