class Bank:
    def __init__(self,accnum,balance,pin):
        self.accnum=accnum
        self._balance=balance #protected attr
        self.__pin=pin #private attr
    def bal(self):
        return self._balance
    def __checkpin(self,entered):
        return entered==self.__pin
    def withdraw(self,amount,entered):
        if self.__checkpin(entered):
            if self._balance>=amount:
                self._balance-=amount
                print("withdrawal of",amount,"successful\nnew balance:",self._balance)
            else:
                print("insufficient balance")
        else:
            print("Incorrect pin")
acc=Bank(9090,5000,2345) #obj
print(acc.accnum)
print(acc._balance) #or acc.bal() #protected attr callable
acc.withdraw(2000,2345)
print(acc.bal())
print(acc.__pin) #private attr not callable
