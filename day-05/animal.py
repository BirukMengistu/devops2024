class Animal:
    def __init__(self, name , age,type='animal'):
        self.type = type
        self.name = name
        self.age = age

    def speak(self, sound=''):
        if sound=='':
         print(f'{self.name} cannot speak')
        else:
         print(f'{self.name} is speaking {sound}')

    def eat(self):
        if self.type == 'carnivore':
            print(f'{self.name} is eating meat')
        elif self.type == 'herbivore':
         print(f'{self.name} cannot eat meat') 
        else:
            print(f'{self.name} is eating')