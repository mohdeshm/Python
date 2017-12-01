from AccountScheduler import  AccountScheduler
class Client:
    def __init__(self):
        self.accountScheduler = ""

    def showTransactions(self):
        self.accountScheduler=AccountScheduler()
        while(True):
            choice=input("Enter the choice of operation\n1.Create Account\n2.Deposit Amount\n3.Withdraw Amount\n4.Fund transfer\n5.Exit")
            if(choice==1):
                try:
                    accountNo = input("Enter an accountNo")
                    custName = raw_input("Enter the name of customer")
                    self.accountScheduler.createAccount(accountNo, custName, 0)
                except SyntaxError, NameError:
                    print "Error: The number  can't contain special symbols or alphabets"
                else:
                    print("Unknown Error")
                continue

            elif(choice==2):
                try:
                    accountNo=raw_input("Enter your accountNo")
                    amount=input("Enter the amount you want to deposit")
                    self.accountScheduler.depositAmount(amount,accountNo)
                except KeyError:
                    print "Error: Account Does Not Exist"
                else:
                    print
                    continue

            elif(choice==3):
                accountNo=raw_input("Enter your accountNo")
                amount = input("Enter the amount you want to withdraw")
                self.accountScheduler.withDrawAmount(amount,accountNo)
                continue

            elif(choice==4):
                fromAccountNo=raw_input("Enter the accountNo from where the money is to be transferred")
                toAccountNo=raw_input("Enter the accountNo to which the money is to be transferred")
                amount=input("Enter the amount ot be transferred")
                self.accountScheduler.fundTransfer(fromAccountNo,toAccountNo,amount)
                continue

            elif(choice==5):
                break

client=Client()
client.showTransactions()