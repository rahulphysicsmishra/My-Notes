"""It is used only in indexed attributes like arrays,
  dictionaries, lists etc. Instead of directly accessing
  and manipulating class attributes, it provides such methods
  so these attributes can be modified only by its own instances
  and thus implements abstraction..."""

class bank_record():

    def __init__(self, name):

        self.record = {
            "name": name,
            "balance": 100,
            "transaction": [100]
        }

    def __getitem__(self, key):
        return self.record[key]

    def __setitem__(self, key, newvalue):

        if key == "balance" and newvalue != None and newvalue >= 100:
            self.record[key] += newvalue

        elif key == "transaction" and newvalue != None:
            self.record[key].append(newvalue)

    def getBalance(self):
        return self.__getitem__("balance")

    def updateBalance(self, new_balance):

        self.__setitem__("balance", new_balance)
        self.__setitem__("transaction", new_balance)

    def getTransaction(self):
        return self.__getitem__("transaction")

    def numTransactions(self):
        return len(self.record["transaction"])

sam = bank_record("Sam")
print("The balance is: "+ str(sam.getBalance()))

sam.updateBalance(200)
print("The new balance is: " + str(sam.getBalance()))
print("The no of transactions are: " + str(sam.numTransactions()))


sam.updateBalance(300)
print("The new balance is: " + str(sam.getBalance()))
print("The no of transactions are: " + str(sam.numTransactions()))
print("The transactions history is: " + str(sam.getTransaction()))
