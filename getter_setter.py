class Person:   
     def __init__(self):   
          self._age = 0  
         
     # using the getter function   
     @property  
     def age(self):   
         #print("getter method")   
         return self._age   
         
     #now, using the setter function   
     @age.setter   
     def age(self, x):   
         if(x < 18):   
            print("You are not eligible for voting")   
         #print("setter method") 
         else:
            print("You are eligible for voting")  
         self._age = x   
    
Katha= Person()   
    
Katha.age = int(input("Enter your age to get know about that you are eligible for voting or not"))  
    
#print(Katha.age)   