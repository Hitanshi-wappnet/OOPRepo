#Implement Multiple,Multilevel Inheritence with Access modifiers
#Implement multiple,Muktilevel Inheritence with Polymorphisam i.e. Method Oveloading and Method Overriding

import random

class Bank:
    __bid=str(random.randint(1,100))
    _branch="ahmedabad"
    # def accountcreate(self,fname,lname):
    #     self.fname=fname
    #     self.lname=lname
    #     print(f"Congrartualtion {self.fname} Your account is created and your account no is {self.__bid}")

    def accountcreate(self):
        print("The account is created")

    def _calculateinterest(self,p,r,n):
        self.amount=p
        self.rate=r
        self.time=n
        interest=int((self.amount*self.rate*self.time)/100)
        print(f"Hello {self.fname} , the interest to be deposited into your account_no{self.__id} is {interest}")


class RBI:
    def makefd(self,amount,rate,year):
        self._amount=amount+((amount*rate*year)/100)
        print(f"Greetings! The FD is created and amount you get after {year} with rate {rate} on amount {amount} is {self._amount}")

class HDFC(Bank):
    __id="HDFC_"+str(random.randint(1,100))
    def accountcreate(self,fname,lname):
        super().accountcreate()
        self.fname=fname
        self.lname=lname
        print(f"Congrartualtion {self.fname} Your account is created in HDFC Bank and your account no is {self.__id}")
    def _calculateinterest(self,p,n):
        self.amount=p
        self.time=n
        interest=int((self.amount*int(8)*self.time)/100)
        print(f"Hello, the interest to be deposited into your account_no {self.__id} is {interest}")

class SBI(Bank,RBI):
    def accountcreate(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.__id="SBI_"+str(random.randint(1,100))
        print(f"Congrartualtion {self.fname} Your account is created in SBI Bank and your account no is {self.__id}")
    def _calculateinterest(self,p,n):
        self.amount=p
        self.time=n
        interest=int((self.amount*int(7)*self.time)/100)
        print(f"Hello {self.fname} , the interest to be deposited into your account_no{id} is {interest}")

    def _makefd(self,amount,rate,year):
        self.__amount=amount+((amount*rate*year)/100)
        print(f"Greetings! The FD is created and amount you get after {year} with rate {rate} on amount{amount} is {self._amount}")

class HDFC_Vastral(HDFC):
    def deposit_cheque(self,id,amount):
        print(f"Hello ,amount {amount} is deposited into your account_no{self.__id}")

B=Bank()
H=HDFC()
S=SBI()
hr=HDFC_Vastral()
R=RBI()
H.accountcreate("Hitanshi","Patel")
#S.__makefd(100000,8,10)
R.makefd(100000,5,8)
#B.accountcreate("Amita","Jain")
print(B._branch)
print("Your Branch is",H._branch)
S.accountcreate("Ashneer","Grover")
#S.__makefd(10000,8,5)
H._calculateinterest(10000,8)
hr._calculateinterest(10000,62)
print("Branch is",hr._branch)
#print(S.__bid)