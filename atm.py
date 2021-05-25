

class ATM(object):
    def __init__(self,pin,cardnumber):
        self.pin = input("ENTER PIN ")
        self.cardnumber = input("ENTER CARDNUMBER ")

    def Details(self,pin,cardnumber):
        self.pin = input("ENTER PIN")
        self.cardnumber = input("ENTER CARDNUMBER")

    def GiveDetails(self):
        return self.pin, self.cardnumber
  


banker1 = ATM(1000,1233)
x = banker1.GiveDetails()
print(x)
startMoney = 100


print("Please enter 1 for Cash Withdrawal")
print("Please enter 2 for Cash BalanceEnquiry")
option = input("What option would you like to choose ")

if option == "1":
    def CashWithdrawal():
         withdrawl = float(input('How Much Would you like to withdraw?'))
         balance = startMoney - withdrawl
         print("Now your Balance is ",balance)

CashWithdrawal()


if option == "2":
     def BalanceEnquiry():
         print("Balance is ",balance)

BalanceEnquiry()

       
        
    