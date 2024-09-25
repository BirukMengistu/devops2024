#pyhton loop lection

fruits =['apple', 'banna', 'cherry']

for x in fruits:
  print(x)

print('break statement - banna')
  #break statement
for y in fruits:
  print(y)
  if y == 'banna':
    break

 
print('continue statement -banna')
  # continue statement
  #continue statement we can stop the current iteration of the loop

for y in fruits:
    if y == 'banna':
     continue
    print(x)

#range function

for x in range(5):
  print(x+1)
  x=input('add number')
  
