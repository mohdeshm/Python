from Account import Account
from InsufficientBalanceException import  InsufficientBalanceException
class AccountScheduler:
    def __init__(self):
        self.account = ""
        self.accounts={}

    def createAccount(self,accountNo,custName,balance):
        self.account=Account()
        self.account.setAccountNo(accountNo)
        self.account.setCustName(custName)
        self.account.setBalance(balance)
        self.accounts.update({accountNo:self.account})
        print "Account has been successfully created for account number",accountNo

    def getAccount(self,accountNo):
        self.account=self.accounts[accountNo]
        return self.account

    def depositAmount(self,amount,accountNo):
        self.account=self.accounts[accountNo]
        self.account.setBalance(self.account.getBalance()+amount)
        print("Account balance has been successfully updated to", self.account.getBalance(),
              "for account number", accountNo)
        return self.account

    def withDrawAmount(self,amount,accountNo):

        self.account = self.accounts[accountNo]
        if (amount > self.account.getBalance()):
            raise InsufficientBalanceException
        self.account.setBalance(self.account.getBalance()-amount)
        print("Account balance has been successfully updated to",self.account.getBalance(),
        "for account number",accountNo)
        return self.account


    def fundTransfer(self,fromAccountNo,toAccountNo,amount):
        fromAccount=self.withDrawAmount(amount,fromAccountNo)
        toAccount=self.depositAmount(amount,toAccountNo)