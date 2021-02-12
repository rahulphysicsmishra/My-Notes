# Base class1
class Mother:
    mothername = ""
    def Mother(self):
        print(self.mothername)

# Base class2
class Father:
    fathername = ""
    def Father(self):
        print(self.fathername)

# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father: "+ self.fathername)
        print("Mother: " + self.mothername)

# Driver's code
s1 = Son()
s1.fathername = "Ram"
s1.mothername = "Sita"
s1.parents()



