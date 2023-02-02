#static and classic Methods 

class Car:
    base_price=100000  #Class Variable

    def __init__(self,windows,doors,power): #constructor of class Car
        self.windows=windows
        self.doors=doors
        self.power=power

    def what_base_price(self): #Describe base price for the car
        print(f"The base price is {self.base_price}")

    @classmethod   #class method
    def revise_base_price(cls,increment): #Describe reverse base price for car
        cls.base_price=(cls.base_price +(cls.base_price*increment))
        return cls.base_price

    @staticmethod       #static method
    def check_speed():  #check speed of the car
        speed=int(input("Enter the speed of car you drive"))
        if speed<70:
            print("Your speed is perfect")
        else:
            print("Your speed is too high for driving")

    """ @staticmethod
    def check_condition():
        speed=int(input("Enter the speed of car you drive"))
        if speed<70:
            print("Your car condition is good")
        else:
            print("Your car condition is not good")
         """

#car1=Car(4,5,2000)
car2=Car(3,5,5000)
#Car.base_price=5000000
print(Car.base_price)
Car.check_speed()
#Car.check_condition()
print(Car.revise_base_price(0.12))
print(car2.revise_base_price(0.10))