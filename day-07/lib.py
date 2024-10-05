mystuff =   {'apple': "I AM APPLES Dict!"}
print(mystuff['apple']) # get apple from dict
print(type(mystuff)) # print type of mystuff
print('-'*50)
print('start exec module')
# This is just a variable
def apple():
    print("I AM APPLES Function!")

# This is a variable that is a string
qoutes='Life is short, smile while you still have teeth.'

#this is class
class mystuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
        
    def apple(self):
        print("I AM CLASSY APPLES!")

# test and calss
class song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)