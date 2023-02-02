#Implement Constructors and destruction with Acess Modifiers and Polymorphisam
#Use of Super() Keyword
#Implement both parameterized Constructor and Nonparameterized Construction

import random

class Bank:
    def __init__(self):
        print("Welcome to the world of Bank")

    # def __init__(self,fname): #Constructor
    #     __bid=str(random.randint(1,100))
    #     _branch="ahmedabad"
    #     self.fname=fname
    #     print(f"Your details:\n The id is {__bid} \n The branch is {_branch} \n The name is {self.fname}")

    def _calculateinterest(self,p,r,n): #method for calculating interest
        self.amount=p
        self.rate=r
        self.time=n
        interest=int((self.amount*self.rate*self.time)/100)
        print(f"Hello {self.fname} , the interest to be deposited into your account_no{self.__id} is {interest}")

    def __del__(self):  #Destruction
        print("Object Bank is destroid")

class RBI:
    def __init__(self): #constructor
        print("RBI is the main bank in all the available bank")

    def makefd(self,amount,rate,year):  #method to find amount after making FD
        self._amount=amount+((amount*rate*year)/100)
        print(f"Greetings! The FD is created and amount you get after {year} with rate {rate} on amount {amount} is {self._amount}")

    def __del__(self):
        print("Object RBI is destroid")
  
class HDFC(Bank):
    def __init__(self,acc_type): #constructor of HDFC Class
        __id="HDFC_"+str(random.randint(1,100))
        super().__init__()
        self.account_type=acc_type
        print(f"Congrartualtion  Your account is created in HDFC Bank and your account no is {__id} and the type of your account is {self.account_type}")

    def _calculateinterest(self,p,n): #method to calculate interest from amount aand rate
        self.amount=p
        self.time=n
        interest=int((self.amount*int(8)*self.time)/100)
        print(f"Hello, the interest to be deposited into your account_no {self.__id} with the rate 8% is {interest}")

    def __del__(self):
        super().__del__()
        print("Object HDFC is destroid ")

class SBI(Bank,RBI):
    def __init__(self,acc_type): #constructor of SBI Class
        Bank.__init__(self,"katha")
        RBI.__init__(self)
        self.account_type=acc_type
        self.__id="SBI_"+str(random.randint(1,100))
        print(f"Congrartualtion Your account is created in SBI Bank and your account no is {self.__id} and account type is {self.account_type}")

    def _calculateinterest(self,p,n): #calculate interest
        self.amount=p
        self.time=n
        interest=int((self.amount*int(7)*self.time)/100)
        print(f"Hello {self.fname} , the interest to be deposited into your account_no{id} is {interest}")

    def __makefd(self,amount,rate,year): #calculate FD 
        self._amount=amount+((amount*rate*year)/100)
        print(f"Greetings! The FD is created and amount you get after {year} with rate {rate} on amount{amount} is {self._amount}")

    def __del__(self):
        Bank("Katha").__del__()
        super().__del__()
        print("Object SBI is destroid ")

class HDFC_Branch(HDFC):
    def __init__(self): #constructor of HDFC_Branch
        Bank.__init__(self,"Katha")
        super().__init__("Join account Holder")
        print("Your Branch is switched to Surat")

    def deposit_cheque(self,id,amount): #method to print deposited amount
        print(f"Hello ,amount {amount} is deposited into your account_no{self.__id}")

    
#B=Bank("Namita")
H=HDFC("Saving")
#S=SBI("Current")
# R=RBI()
#hr=HDFC_Branch()