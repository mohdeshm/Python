class Account:
    def __init__(self):
        self.accountNo = 0
        self.custName = ""
        self.balance = 0

    def setAccountNo(self, accountNo):
        self.accountNo = accountNo

    def getAccountNo(self):
        return self.accountNo

    def setCustName(self, custName):
        self.custName = custName

    def getCustName(self):
        return self.custName

    def setBalance(self, balance):
        self.balance = balance

    def getBalance(self):
        return self.balance
