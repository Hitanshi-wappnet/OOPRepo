import random

class Bank:
    _balance=0  #Class Variable
    choice_bank=0  #Class Variable
    _fd_amout=0 #Class Variable
    fd_year=0  #Class Variable

    def __init__(self):
        print("Welcome to the Bank..")
        user_choice=input("Do you want to acess the service of the bank(y/n)")
        if(user_choice=='y'):
            Bank.choice_bank=int(input("You have below available bank to access the service \n 1.HDFC \n 2.SBI \n 3.BOI \n Please enter your Choice Number \n"))
        else:
            print("Thank you for Visiting bank...Have a great day")

class HDFC(Bank):
    #_balance=0  #Class Variable
    fd_rate=10  

    def __init__(self):
        #super().__init__()

        print("Thank You for choicing HDFC Bank..")
        choice=int(input("Welcome to HDFC Bank \n 1.Create New Account \n 2.Display Balance in Account \n 3.Calculate Interest \n 4.Deposit an Amount in Account \n 5.Withdraw an Amount in Account \n 6.Make an FD \n 7.Dispaly Maturity Amount of FD \n Press according to your choice \n"))

        def create_account(self):  #create Account with User Name
            user_name=input("Enter your name\n")
            __acc_id="HDFC_"+str(random.randint(1,1000))
            print(f"Congratulation {user_name} Your account is created with account number {__acc_id}")

        def display_balance(self):   #display balance of User
            #_input_id=input("Enter your account number")
            print(f"Your available balance is {HDFC._balance}\n")

        def calculate_interst(self):    #calculate intersert only at the bank rate
            amount=int(input("Enter Your amount\n"))
            year=int(input("How many year you want to count to calculate interest\n"))
            HDFC_interest=(amount*8*year)/100
            print(f"The interst on {amount} at rate of 8% on year {year} is {HDFC_interest}")

        def deposit_amount(self):   #deposit particular amount in bank account
            #_input_id=input("Enter your Account Number")
            depo_amount=int(input("Enter amount you want to deposit\n"))
            HDFC._balance=HDFC._balance+depo_amount
            print(f"Now your Available balance is {HDFC._balance}")

        def withdraw_amount(self):  #withdraw amount from bank account
            withdraw_amount=int(input("Enter amount you want to withdraw\n"))
            if(withdraw_amount<=HDFC._balance):
                #_input_id=input("Enter your Account Number")
                HDFC._balance=HDFC._balance-withdraw_amount
                print(f"Now your Available balance is {HDFC._balance}")
            else:
                print("The balance is not available in your account")

        def _make_fd(self):
            HDFC._fd_amount=int(input("Enter amount you want to put in FD\n"))
            HDFC.fd_year=int(input("For How many year do you want to make FD\n"))
            print(f"Congratulation!!You make a FD of {HDFC._fd_amount} for {HDFC.fd_year} year")
            
        def display_fd_amount(self):
            HDFC._fd_amount=HDFC._fd_amount+(HDFC._fd_amount*HDFC.fd_rate*HDFC.fd_year)
            print(f"Your Maturity Amount after {HDFC.fd_year} is {HDFC._fd_amount}")

        if(choice==1):
            create_account(self)
                        
        elif(choice==2):
            display_balance(self)
                
        elif(choice==3):
            calculate_interst(self)
                
        elif(choice==4):
           deposit_amount(self)
               
        elif(choice==5):
            withdraw_amount(self)

        elif(choice==6):
            _make_fd(self)

        elif(choice==7):
            display_fd_amount(self)

        else:
            print("You might entered Wrong Choice...")

class SBI(Bank):
    #_balance=0 #Class Variable
    fd_rate=8  #Class Variable

    def __init__(self):
        #super().__init__()

        #if(super().choice_bank==1):
        print("Thank You for choicing SBI Bank..")
        choice=int(input("Welcome to SBI Bank \n 1.Create New Account \n 2.Display Balance in Account \n 3.Calculate Interest \n 4.Deposit an Amount in Account \n 5.Withdraw an Amount in Account \n 6.Make an FD \n 7.Dispaly Maturity Amount of FD \n Press according to your choice \n "))

        def create_account(self):   #create Account with User Name
            user_name=input("Enter your name\n")
            __acc_id="SBI_"+str(random.randint(1,1000))
            print(f"Congratulation {user_name} Your account is created with account number {__acc_id}")

        def display_balance(self):  #display balance of User
            #_input_id=input("Enter your account number")
            print(f"Your available balance is {SBI._balance}")

        def calculate_interst(self):    #calculate intersert only at the bank rate
            amount=int(input("Enter Your amount\n"))
            year=int(input("How many year you want to count to calculate interest\n"))
            SBI_interest=(amount*6*year)/100
            print(f"The interst on {amount} at rate of 6% on year {year} is {SBI_interest}")

        def deposit_amount(self):   #deposit particular amount in bank account
            #_input_id=input("Enter your Account Number")
            depo_amount=int(input("Enter amount you want to deposit\n"))
            SBI._balance=SBI._balance+depo_amount
            print(f"Now your Available balance is {SBI._balance}")

        def withdraw_amount(self):  #withdraw amount from bank account
            withdraw_amount=int(input("Enter amount you want to withdraw\n"))
            if(withdraw_amount<=self._balance):
                #_input_id=input("Enter your Account Number")
                SBI._balance=SBI._balance-withdraw_amount
                print(f"Now your Available balance is {SBI._balance}")
            else:
                print("The balance is not available in your account")

        def _make_fd(self):
            SBI._fd_amount=int(input("Enter amount you want to put in FD\n"))
            SBI.fd_year=int(input("For How many year do you want to make FD\n"))
            print(f"Congratulation!!You make a FD of {SBI._fd_amount} for {SBI.fd_year} year")

        def display_fd_amount(self):
            SBI._fd_amount=SBI._fd_amount+(SBI._fd_amount*SBI.fd_rate*SBI.fd_year)
            print(f"Your Maturity Amount after {SBI.fd_year} is {SBI._fd_amount}")

        if(choice==1):
            create_account(self)
                        
        elif(choice==2):
            display_balance(self)
                
        elif(choice==3):
            calculate_interst(self)
                
        elif(choice==4):
           deposit_amount(self)
               
        elif(choice==5):
            withdraw_amount(self)
        
        elif(choice==6):
            _make_fd(self)

        elif(choice==7):
            display_fd_amount(self)

        else:
            print("You might entered Wrong Choice...")

class BOI(Bank):
    #_balance=0   #Class Variable
    fd_rate=9

    def __init__(self):
        #super().__init__()

        #if(super().choice_bank==1):
        print("Thank You for choicing BOI Bank..")
        choice=int(input("Welcome to BOI Bank \n 1.Create New Account \n 2.Display Balance in Account \n 3.Calculate Interest \n 4.Deposit an Amount in Account \n 5.Withdraw an Amount in Account \n 6.Make an FD \n 7.Dispaly Maturity Amount of FD \n Press according to your choice \n"))

        def create_account(self):   #create Account with User Name
            user_name=input("Enter your name\n")
            __acc_id="BOI_"+str(random.randint(1,1000))
            print(f"Congratulation {user_name} Your account is created with account number {__acc_id}")

        def display_balance(self):  #display balance of User
            #_input_id=input("Enter your account number")
            print(f"Your available balance is {BOI._balance}")

        def calculate_interst(self):    #calculate intersert only at the bank rate
            amount=int(input("Enter Your amount\n"))
            year=int(input("How many year you want to count to calculate interest\n"))
            BOI_interest=(amount*7*year)/100
            print(f"The interst on {amount} at rate of 7% on year {year} is {BOI_interest}")

        def deposit_amount(self):   #deposit particular amount in bank account
            #_input_id=input("Enter your Account Number")
            depo_amount=int(input("Enter amount you want to deposit\n"))
            BOI._balance=BOI._balance+depo_amount
            print(f"Now your Available balance is {BOI._balance}")

        def withdraw_amount(self):  #withdraw amount from bank account
            withdraw_amount=int(input("Enter amount you want to withdraw\n"))
            if(withdraw_amount<=self._balance):
                #_input_id=input("Enter your Account Number")
                BOI._balance=BOI._balance-withdraw_amount
                print(f"Now your Available balance is {BOI._balance}")
            else:
                print("The balance is not available in your account")

        def _make_fd(self):
            BOI._fd_amount=int(input("Enter amount you want to put in FD\n"))
            BOI.fd_year=int(input("For How many year do you want to make FD\n"))
            print(f"Congratulation!!You make a FD of {BOI._fd_amount} for {BOI.fd_year}")

        def display_fd_amount(self):
            BOI._fd_amount=BOI._fd_amount+(BOI._fd_amount*BOI.fd_rate*BOI.fd_year)
            print(f"Your Maturity Amount after {BOI.fd_year} is {BOI._fd_amount}")

        if(choice==1):
            create_account(self)
                        
        elif(choice==2):
            display_balance(self)
                
        elif(choice==3):
            calculate_interst(self)
                
        elif(choice==4):
           deposit_amount(self)
               
        elif(choice==5):
            withdraw_amount(self)

        elif(choice==6):
            _make_fd(self)

        elif(choice==7):
            display_fd_amount(self)

        else:
            print("You might entered Wrong Choice...")

B=Bank()           
ch=Bank.choice_bank
if(ch==1):
    while(1):
        H=HDFC()
        prefer=int((input("If you want to continue This Service Then Press 1 And if you don't want then Press 0\n")))
        if(prefer==0):
            exit()
if(ch==2):
    while(1):
        S=SBI()
        prefer=int((input("If you want to continue This Service Then Press 1 And if you don't want then Press 0\n")))
        if(prefer==0):
            exit()
if(ch==3):
    while(1):
        B=BOI()
        prefer=int((input("If you want to continue This Service Then Press 1 And if you don't want then Press 0\n")))
        if(prefer==0):
            exit()
