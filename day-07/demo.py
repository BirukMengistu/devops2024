
import lib
# This is an example of a function that takes a dictionary as an argument
my_stuff = lib.mystuff
app_def= lib.apple
qoutes_life = lib.qoutes
#print(my_stuff['apple'])
print(app_def)
print(qoutes_life)

print('-'*50)
print("import class and reuse it")
item= lib.mystuff()
item.apple()
print(item.tangerine)

print('-'*50)
print("import class and reuse from Song class 1st instance")
print('\n'*2)
happy_bday = lib.song(["Happy birthday to you", 
                       "I don't want to get sued", 
                       "So I'll stop right there"])

print('1st instance of song class')
happy_bday.sing_me_a_song()

print("import class and reuse from Song class")
print('\n'*2)
print('2nd instance of song class')
# bulls_on_parade= lib.song() 
# #print('1st instance of song class')

bulls_on_parade = lib.song(["They rally around the family",
                            "With pockets full of shells"])
bulls_on_parade.sing_me_a_song()

print('\n'*2)