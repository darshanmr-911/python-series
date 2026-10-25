<<<<<<< HEAD
class Car:
    def __init__(self,car_id,name,year,price_per_day,status="available",rented_days=0):
        self.car_id=car_id
        self.name=name
        
        self.year=year
        self.price_per_day=price_per_day
        self.status=status
        self.rented_days=rented_days
    def display_details(self):
        print(f"Car ID:{self.car_id},Name:{self.name},Year:{self.year},Status:{self.status}")
    def update(self,new_status):
        self.status=new_status
        print(f"Car ID{self.car_id} Status updated to {self.status}")
    def price(self):
        total_price=self.price_per_day*self.rented_days
        print(f"Total Rented Price for {self.name}:{total_price}$")
car1 = Car(1, 'swift', 2019, 50, rented_days=9)
car2=Car(2,'bmw',2019,50,'rented',3)
car3=Car(3,'ford',2019,3)
car1.display_details()
car2.update("available")
car3.price()
car1.price()
=======
def greet(name):
    x
>>>>>>> master
