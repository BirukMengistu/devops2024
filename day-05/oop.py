item1 ='phone'
item_price =100
item_quantity = 3
item1_price_total = item_price * item_quantity
print(item1_price_total)
print(type(item1_price_total))


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f'instatance of Item ,{self.name}, {self.price}, {self.quantity}')
    def config(self):
        print(f'config method, {self.name}, {self.price}, {self.quantity}') 
    def total(self):
        return self.price * self.quantity



objItem = Item('phone', 100, 3) # type: ignore
objItem1= Item('laptop', 400, 3) 
objItem.test = 'test'


Item.config(objItem)
Item.config(objItem1)

kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]