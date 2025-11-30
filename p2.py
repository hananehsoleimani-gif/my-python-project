#create a class for product(parent class)
class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = price

#create a child class(Electronics and Clothes)
"""I used get_info() method to show how polymorphism work 
   both of them share the same name but doing the different things"""
class Electronics(Products):
    def __init__(self, name, price , warranty):
        super().__init__(name , price)
        self.warranty = warranty
    def get_info(self):
        return f"{self.name}-${self.price}-${self.warranty}"
class Clothes(Products):
    def __init__(self , name, price , size , color):
        super().__init__(name , price)
        self.size = size
        self.color = color

    def get_info(self):
        return f"{self.name}-${self.price}-${self.size}-{self.color}"
#build cart class for store list of products
#using list for add or remove items
#remove_product() method for remove and add_product() for add
class Cart:
    def __init__(self):
        self.items=[]
    def add_product(self,product):
        self.items.append(product)
    def remove_product(self,product):
        if product in self.items:
            self.items.remove(product)
        else:
            print("Product not available")
#calculated total price
    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
#displays the products currently in the cart along with their prices
    def show_cart(self ):
        print("cart contents:")
        for item in self.items:
            print(f"{item.name}-${item.price}")

pant=Clothes("PANT" , 150 , 42,"blue")
laptop = Electronics("LAPTOP" , 1000000, "18 month")
shoes = Clothes("SHOES",280,"small","red")

cart = Cart()

cart.add_product(laptop)
cart.add_product(shoes)


cart.show_cart()


print(f"Total price: {cart.total_price()}")
