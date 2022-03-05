class bank:
    def __init__(self, acc, name, type, bal):
        self.acc = acc
        self.name = name
        self.type = type
        self.bal = bal

    def depositFn(self, dep_amnt):
        self.bal += dep_amnt
        print("The updated balance is : ", self.bal)

    def widthDrawFn(self, with_amnt):
        if self.bal < with_amnt:
            print("Invalid !! Insufficient balance !!")
        else:
            self.bal -= with_amnt
        print("The updated balance is : ", self.bal)

    def displayFn(self):
        print("Acc No:", self.acc)
        print("Name:", self.name)
        print("Acc Type:", self.type)
        print("Acc Balance:", self.bal)


acc_no = int(input("Please enter your Account No. : "))
name = input("Please enter your name : ")
acc_type = input("Please enter your account type : ")
acc_bal = int(input("Please enter your current balance : "))

obj1 = bank(acc_no, name, acc_type, acc_bal)
obj1.displayFn()

dep_amnt = int(input("\nEnter the amount to deposit in the bank : "))
obj1.depositFn(dep_amnt)

with_amnt = int(input("\nEnter the amount to withdrawal from the bank : "))
obj1.widthDrawFn(with_amnt)
