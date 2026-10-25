class mobile:
    def __init__(self,brand,price,model):
        self.model=model
        self.brand=brand
        self.price=price
    def display(self):
        print("Name of the Brand:",self.brand)
        print("Price of the brand:",self.price)
        print("Model of the brand:",self.model)
s1=mobile("IPHONE",'90k',19)
s1.display()