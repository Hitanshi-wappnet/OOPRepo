'''
Implemented abstract class with abstract methods and concrete methods with car example
'''

import abc
from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

    #Concrete Methods
    def features(self):
        print("The Features are available:Backup Camera,Navigation Systems,Leather Seats,Blueetooth")

class Tesla(Car):
    #Overriding abstarct method
    def mileage(self):
        print("The mileage of Tesla is 90 kmh")

    #Overriding Concrete Method
    def features(self):
      print("The Features are available:Automation,Backup Camera,Navigation Systems,Leather Seats,Blueetooth")

class Suzuki(Car):
    #Overriding abstarct method
    def mileage(self):
        print("The mileage of Suzuki car is 80 kmh")

class I10(Car):
    #Overriding abstarct method
    def mileage(self):
        print("The mileage of  car is 50 kmh")

class Duster(Car):
    #Overriding abstarct method
    def mileage(self):
        print("The mileage of Suzuki car is 70 kmh")

T=Tesla()
S=Suzuki()
I=I10()
D=Duster()
T.mileage()
S.mileage()
T.features()

