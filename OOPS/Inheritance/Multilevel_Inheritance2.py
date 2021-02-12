# Base class
class Grandfather:
    grandfathername = ""
    def grandfather(self):
        print(self.grandfathername)

# Intermediate class
class Father(Grandfather):
    fathername = ""
    def father(self):
        print(self.fathername)

# Derived class
class Son(Father):
    def parent(self):
        print("Grandfather: " + self.grandfathername)
        print("Father: " + self.fathername)

# Driver's code
s1 = Son()
s1.grandfathername = "Bramha"
s1.fathername = "Manu"
s1.parent()
